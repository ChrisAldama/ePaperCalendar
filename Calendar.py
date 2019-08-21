# This Python file uses the following encoding: utf-8
import os.path
import pickle
from datetime import datetime
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


class Calendar:
    def __init__(self):
        self.scopes = ['https://www.googleapis.com/auth/calendar.readonly']
        self.creds = self.getCreds()
        self.service = build('calendar', 'v3', credentials=self.creds)

    def getCreds(self):
        if hasattr(self, 'creds'):
            if not self.creds.valid:
                self.creds = self.creds.update(Request())
            return self.creds
        if os.path.isfile('token.pickle'):
            with open('token.pickle', 'rb') as token:
                return pickle.load(token)
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', self.scopes)
        creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
        return creds

    def events(self, dateRange):
        events = self.service.events()
        events_result = events.list(calendarId='primary',
                                    timeMin=dateRange[0],
                                    timeMax=dateRange[1],
                                    singleEvents=True,
                                    orderBy='startTime')
        events = events_result.execute().get('items', [])
        return EventList(events)

class EventList:
    def __init__(self, events):
        self.order(events)

    def __getitem__(self, key):
        if key in self.events:
            return self.events[key]
        return None

    def order(self, events):
        self.events = {}
        for e in events:
            start =  e['start']['dateTime']
            start = datetime.strptime(start, '%Y-%m-%dT%H:%M:%S%z')
            key = (start.hour, start.weekday())
            self.events[key] = e['summary']


