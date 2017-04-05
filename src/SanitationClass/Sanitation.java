//import org.json.JSONArray;
//import org.json.JSONException;
//import org.json.JSONObject;

class Sanitation {
	public static void main(String[] args) {
		//Really Random String for Testing, probably not valid bu anyways
<<<<<<< HEAD
		String JSONString = "{\"Location_result\":[{\"msg\":{\"sta_eth_mac\": {\"addr\": \"1e:06:2a:1c:be:3b\"},\"sta_location_x\": \"5\",\"sta_location_y\": \"7\",\"error_level\": 9,\"associated\": true,\"campus_id\": \"08FBBBBF81D937759B5DAC4963DFBC1A\",\"building_id\": \"24C73B58A1F33C3ABE427485A9977BFF\",\"floor_id\": \"D635A61B06673775ADFF61D70B55785C\",\"hashed_sta_eth_mac\": \"A09B5D8F99F9BB8034A8ADBBEC11B24494981096\",\"geofence_ids\": true,\"loc_algorithm\": \"ALGORITHM_CALIBRATION\",\"longitude\": \"-122.008\",\"latitude\": \"37.4129\",\"altitude\": 5,\"unit\": \"METERS\"},\"ts\": 1434750262}]} \n";
=======
		String JSONString = "{ ID: '559872', Longitude: 1233415, Latitude: 22141455, Altitude: 3368, MyLittlePony: 1 }";
>>>>>>> wip
		System.out.println("Testing");
		System.out.println("Begin Cleaning JSON string");
		System.out.println(JSONString);

		String newJSON = Sanitation.cleanJSONString(JSONString);

		System.out.println(newJSON);
		System.out.println("End Test");
	}

	//Will make more functions for each type of clean up that needs to be done
	static String cleanJSONString(String _json) {
		String returnVal = "Error";
		try {
			//If any variable names change then just change the strings inside the get functions parameter
			JSONObject jsonObject = new JSONObject(_json);
			JSONArray strip1 = jsonObject.getJSONArray("Location_result");
			JSONObject strip2 = strip1.getJSONObject(0);
			int ts = strip2.getInt("ts");
			JSONObject strip3 = strip2.getJSONObject("msg");
			JSONObject strip4 = strip3.getJSONObject("sta_eth_mac");
			//System.out.println(strip4.toString());

			String longitude = strip3.getString("longitude");
			String latitude = strip3.getString("latitude");
			String macAddress = strip4.getString("addr");

			returnVal = "{ \"TimeStamp\": " + ts + ", \"MacAddress\": \"" + macAddress + "\", \"x\": \"" + longitude + "\", \"y\": \"" + latitude + "\" }";
		} catch (JSONException e) {
			System.out.println(e.getMessage());
			return null;
		}
		return returnVal;
	}
}