
import requests
from datetime import datetime
from requests.exceptions import Timeout, RequestException, HTTPError


class ObservingTraffic: 
    ''' This is the first class, in order to record the 15 minute traffic observation, collecting the site of where the observation was, the date of the observation, the timestamp of when the observation ended, the average speed of all of the vechiles crossed at the site in this time frame, and the amount of vechiles that have passed in this time frame '''
    def __init__(self, site, date, times, speed, volume):
        '''This constructor stores a single traffic observation with its site, date, time, speed, and volume.'''
        self.site = site
        self.date = date
        self.times = times
        self.speed = speed
        self.volume = volume

    def is_valid(self) -> bool: 
        ''' The method "is valid" checks to see if the data recorded at the sites are usable'''
        return self.speed is not None and self.volume is not None

    def __lt__(self, other: object) -> bool: 
        ''' The less than function allows to sort all of the collected data in chronological order of what exact times the data was collected, to see the full report at the end in chronological order '''
        if not isinstance (other, ObservingTraffic):
            return NotImplemented
        return self.times < other.times
    
    def __eq__(self, other: object) -> bool: 
        ''' Checking to see if the two times should be consdiered the same object in the system if they have the exact same data '''
        if not isinstance(other, ObservingTraffic):
            return NotImplemented
        return (self.site, self.date, self.times) == (other.site, other.date, other.times)

    __hash__ = None #This makes it explicity unhashable, so there is no hash contract to worry about 


    def __repr__(self) -> str:
        ''' This will return and organized and readable representation of the data collected at the site '''
        return f"[{self.date} {self.times}] Site = {self.site}, Speed = {self.speed} mph, Volume = {self.volume}" 


class FetchingData: 
    '''The fetching data class was created in order to connect with the WebTris API, it goes to the API and asks for the data at whatever site, our system needs for the current case and then the API sends the raw JSON data(which is the raw data before this program anaylsis's it) and with this raw data, it will be passed to the ClientReport class to be converted into objects so that these objects can be used in the traffic class, to be stored''' 
    baseline = "https://webtris.nationalhighways.co.uk/api/v1.0" #This is WebTris API address, so we can request data

    def fetch_daily_report(self, site_id: str, report_date: str):
        '''This method makes the API call, in order to get the raw JSON data'''
        url = f"{self.baseline}/reports/daily" #This url gives the daily report of different sites and which days report we want 
        params = {
            "sites": site_id,
            "start_date": report_date,
            "end_date": report_date,
            "page": 1,
            "page_size": 500,
        }
        try:
            response = requests.get(url, params=params, timeout=15) #This actually gets the request(using the get request), it waits up to 15 seconds before returning whatever error, which then we go on to handling the errors 
            if 202 <= response. status_code < 300: #Prints if the status code is between 202 and 300 which are all sucessful responses
                return {"error": f"Non-standard: {response.status_code}"}
            if 300 <= response.status_code < 400: #Prints if the status code is between 300 and 400 which are all redirect responses
                return {"error": f"Redirect occurred: {response.status_code}"}
            response.raise_for_status() #This line detect the 400 and 500 error codes so that we do not need to write a bunch of if else statements having the computer go through all of the possible errors, and it automatically raises an HTTPError 
            return response.json() # If there is no error after getting the data, then the raw JSON data will go on to be to turned into objects, so that be easier to process and use the data 
        except Timeout: #Now we are handling errors and exceptions and the timeout error happens if the response takes longer than 15 seconds
            return {"error": "Could not connect to the WebTRIS API"}
        except HTTPError as e: #We need this because even through there is the raise_for_status line, to detect 400 and 500 errors, we need to actual handle the errors and this helps make it so the code doesnt crash, but instead raise a cleaner error 
            return {"error": f"HTTP error occurred: {e.response.status_code}"}
        except RequestException as e: #This is a network error, connection dropping with different types of connectivity errors 
            return {"error": f"Network error: {e}"}
        
        


class ClientReport: 
    '''This class takes the raw JSON data(that sucessfully got read) and then we turn it into objects to analyze''' 
    def __init__(self, fetching_API: FetchingData) -> None: 
        ''' this constructor has the data we fetched from the API stored as a reference, allowing the class to call the API '''
        self.fetching_API = fetching_API 

    def get_daily_observations(self, sites, date) -> list[ObservingTraffic]: 
        ''' This called the API, and also returns the raw JSON dictionary '''
        raw_JSON = self.fetching_API.fetch_daily_report(sites, date)
        observations = [] #The list to store the raw data that got converted into objects 

        for row in raw_JSON.get("Rows", []): #Loops through each row of data returned by the API 
            sites = row.get("Site Name") 
            date = row.get("Date of Report")
            time = row.get("Timing")
            speed = row.get("Average Speed")
            volume = row.get("Total Volume of Vehicles")
    
            if not all([sites, date, time, speed, volume]): #If there is data missing from the 3 most important
                continue

            report_date_obj = datetime.fromisoformat(date).date() # got this from (stack overflow)
            try: #Converts speed and volume to numeric values to then evaluate for futher use 
                average_speed = float(row.get("Numerical mph", ""))
                total_volume = int(row.get("Total Volume", ""))
            except ValueError:
                average_speed = None
                total_volume = None

            observations.append(ObservingTraffic(sites, report_date_obj, time, average_speed, total_volume)) ## Create an observing_traffic object from the cleaned and validated row data.

        return sorted(observations) #Sorting all of the observations sorted in order in chronological order 


class TrafficAnalysis: 
    ''' Takes the observations that are converted now into objects and analyzes them '''

    def __init__(self, site_id, site_name) -> None:
        self.site_id = site_id
        self.site_name = site_name
        self.observations: list[ObservingTraffic] = []

    def fetch_data(self, client: ClientReport, report_date: str) -> None:
        '''Fetching data for communicating with API'''
        self.observations = client.get_daily_observations(self.site_id, report_date)

    def average_speed(self) -> float | None:
        '''Returns the average speed across all observation and returns none if there is not any'''
        speeds = [obs.speed for obs in self.observations if obs.is_valid()]
        if not speeds:
            return None
        return sum(speeds) / len(speeds)

    def total_vehicles(self) -> int:
        '''Returns the average vehicles across all valid observations '''
        return sum(obs.volume for obs in self.observations if obs.is_valid())

    def records_for_hour(self, hour: int) -> list[ObservingTraffic]:
        '''Retriving all records in a given hour'''
        return [observation for observation in self.observations if observation.is_valid() and int(observation.times.split(":")[0]) == hour]

    def average_speed_for_hour(self, hour: int) -> float | None:
        '''Returns the average speed for a specific hour, or None if no data exists.'''
        records = self.records_for_hour(hour)
        if not records:
            return None
        return sum(observation.speed for observation in records) / len(records)
        
    def total_vehicles_for_hour(self, hour: int) -> int:
        '''Returns the total number of vehicles recorded during a specific hour.'''
        return sum(observation.volume for observation in self.records_for_hour(hour))

    def peak_hour(self) -> int | None:
        '''Finds the hour with the highest total vehicle count, or None if no data exists.'''
        volumes = {h: self.total_vehicles_for_hour(h) for h in range(24) if self.total_vehicles_for_hour(h) > 0}
        if not volumes:
            return None
        return max(volumes, key=lambda h: volumes[h])
    
    def __iter__(self):
        '''Allows the traffic object to be looped through to be sorted in chronological order.'''
        return iter(sorted(self.observations))

    def __len__(self) -> int:
        '''Returns how many observations are stored for this site.'''
        return len(self.observations)
