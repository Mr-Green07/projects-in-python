   while True:
        print("Listening....")
        query = takecommand()
        sites = [ ["youtube", "https://youtube.com"], ["google", "https://google.com"], ["wikipedia", "www.wikipedia.com"]]
        for site in sites:
            if f"Open {sites[0]})".lower() in query.lower():
                speaker.speak(f"opening {sites[0]}")
                webbrowser.open("https://youtube.com")
     