import requests

def api_service(query):
    try:
        url = "https://tor.publicbikesystem.net/ube/gbfs/v1/en/station_information.json"
        response = requests.get(url, timeout=5)
        data = response.json()

        stations = data["data"]["stations"]

        q = query.lower()

        # If no meaningful keyword, fallback to sample
        if len(q.strip()) < 3:
            selected = stations[:5]
        else:
            # filter stations that match query words
            selected = [
                s for s in stations
                if q in s.get("name", "").lower()
                or any(word in s.get("name", "").lower() for word in q.split())
            ]

            # fallback if nothing matches
            if not selected:
                selected = stations[:5]

        output = "🚲 Relevant Bike Share Stations:\n"

        for s in selected[:5]:
            name = s.get("name", "Unknown station")
            address = s.get("address", "No address")
            output += f"- {name} ({address})\n"

        return output

    except Exception as e:
        return f"API error: {str(e)}"