#!/usr/bin/env python3

import os
import httpx

def main():
    usersteamnumber = "XXX" # My profile to test.
    gameidnumber = 613830 # Chrono Trigger to test
    apikey = "ABC123"

    # url = f"https://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v0001/?appid={gameidnumber}&key={apikey}&steamid={usersteamnumber}"
    url = f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={apikey}&steamid={usersteamnumber}&format=json&include_appinfo=true"
    response = httpx.get(url)
    user_game_data = response.json()
    print(user_game_data["response"]["games"][0]["name"])
    
if __name__ == "__main__":
   main()