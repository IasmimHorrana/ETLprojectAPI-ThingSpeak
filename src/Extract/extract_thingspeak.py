#Extração dados IoT Thingspeak 
import pandas as pd
import requests

def extract_thingspeak(api_key, channel_id, start_date=None, end_date=None):
    """
    Extracts data from a ThingSpeak channel.
    
    Parameters:
    - api_key: str, the API key for the ThingSpeak channel.
    - channel_id: str, the ID of the ThingSpeak channel.
    - start_date: str, optional, the start date for filtering data (format: 'YYYY-MM-DD').
    - end_date: str, optional, the end date for filtering data (format: 'YYYY-MM-DD').
    
    Returns:
    - pd.DataFrame: DataFrame containing the extracted data.
    """
    
    url = f"https://api.thingspeak.com/channels/{channel_id}/feeds.json?api_key={api_key}&results=1000"
    
    if start_date and end_date:
        url += f"&start={start_date}T00:00:00Z&end={end_date}T23:59:59Z"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data['feeds'])
        return df
    else:
        raise Exception(f"Error fetching data from ThingSpeak: {response.status_code}")