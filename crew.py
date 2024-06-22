from crewai import Crew,Process
from agents import tripagents
from tasks import triptasks
# from dotenv import load_dotenv
# load_dotenv()
class TripCrew:
    def __init__(self, origin, cities, date_range, interests):
        self.cities = cities
        self.origin = origin
        self.interests = interests
        self.date_range = date_range

    def run(self):
        agents = tripagents()
        tasks = triptasks()

        city_selector_agent = agents.City_selection_expert()
        local_expert_agent = agents.local_tour_guide()
        travel_concierge_agent = agents.expert_travel_agent()

        identify_city = tasks.identify_city(
            city_selector_agent,
            self.origin,
            self.cities,
            self.interests,
            self.date_range
        )
        gather_city_information= tasks.gather_city_information(
            local_expert_agent,
            self.origin,
            self.interests,
            self.date_range
        )
        plan_itinerary = tasks.plan_itinerary(
            travel_concierge_agent, 
            self.origin,
            self.interests,
            self.date_range
        )



        crew=Crew(
            agents=[city_selector_agent,city_selector_agent,travel_concierge_agent],
            tasks=[plan_itinerary,identify_city,gather_city_information],
            process=Process.sequential,
            memory=False,
            cache=True,
            max_rpm=100,
            share_crew=True
        )

        result=crew.kickoff()
        return(result)
from textwrap import dedent
if __name__ == "__main__":
  print("## Welcome to Trip Planner Crew")
  print('-------------------------------')
  location = input(
    dedent("""
      From where will you be traveling from?
    """))
  cities = input(
    dedent("""
      What are the cities options you are interested in visiting?
    """))
  date_range = input(
    dedent("""
      What is the date range you are interested in traveling?
    """))
  interests = input(
    dedent("""
      What are some of your high level interests and hobbies?
    """))
  
  trip_crew = TripCrew(location, cities, date_range, interests)
  result = trip_crew.run()
  print("\n\n########################")
  print("## Here is you Trip Plan")
  print("########################\n")
  print(result)