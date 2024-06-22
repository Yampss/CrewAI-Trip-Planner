from crewai import Task
from tools import search_tool
from agents import tripagents
class triptasks():
  def identify_city(self,agent,origin, cities, travel_dates, interests):
      # agent=tripagents.City_selection_expert()
      return Task(
          
          description=("""    
          Analyze and select the best city for the trip based on specific
                              criteria such as weather patterns, seasonal events, and travel costs.
                              This task involves comparing multiple cities, considering factors like current weather
                              conditions, upcoming cultural or seasonal events, and overall travel expenses.
                              Your final answer must be a detailed report on the chosen city,
                              including actual flight costs, weather forecast, and attractions.
          **Parameters**:  
          Origin: {origin}                 
          Cities: {cities}
          Travel Date: {travel_dates}
          Interests: {interests}
        """),
        expected_output='Select the best city to travel to ',
        tool=[search_tool],
        async_execution= False,
        agent=agent,
      )
  def gather_city_information(self,agent,city, travel_dates, interests):
      # agent=tripagents.local_tour_guide()
      return Task(
          description=("""        
          **Task**:gather in detail city guide information        
          **Description**: Compile an in-depth guide for the selected city, gathering information about
                          key attractions, local customs, special events, and daily activity recommendations.
                          This guide should provide a thorough overview of what the city has to offer, including
                          hidden gems, cultural hotspots, must-visit landmarks, weather forecasts, and high-level cost
          **Parameters**:                   
          Cities: {city}
          Travel Date: {travel_dates}
          Interests: {interests}
        """),
        expected_output='gather in detail city guide information  ',
        tool=[search_tool],
        async_execution= False,
        agent=agent,
      )

  def plan_itinerary(self,agent,city, travel_dates, interests):
      # agent=tripagents.expert_travel_agent()
      return Task(
          description=("""        
          Expand the city guide into a full 7-day travel itinerary with detailed
              per-day plans, including weather forecasts, places to eat, packing suggestions,
              and a budget breakdown. You MUST suggest actual places to visit, actual hotels to stay,
              and actual restaurants to go to. This itinerary should cover all aspects of the trip,
              from arrival to departure, integrating the city quide information with practical travel logistics.
          **Parameters**:                   
          City: {city}
          Trip Date: {travel_dates}
          Traveler Interests: {interests}
        """),
        expected_output='develop a detailed 7 day itinerary',
        tool=[search_tool],
        agent=agent,
        output_file='itinerary-report.md'
      )