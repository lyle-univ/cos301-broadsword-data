//import org.json.JSONArray;
//import org.json.JSONException;
//import org.json.JSONObject;

class Sanitation {
	public static void main(String[] args) {
		//Really Random String for Testing, probably not valid bu anyways
		String JSONString = "{ ID: '559872', Longitude: 1233415, Latitude: 22141455, Altitude: 3368, MyLittlePony: 1 }";
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
			String userID = jsonObject.getString("ID");
			//System.out.println(userID);

			int longitude = jsonObject.getInt("Longitude");
			//System.out.println(longitude);

			int latitude = jsonObject.getInt("Latitude");
			//System.out.println(latitude);

			int altitude = jsonObject.getInt("Altitude");
			//System.out.println(altitude);

			returnVal = "{ ID: '" + userID + "', Longitude: " + longitude + ", Latitude: " + latitude + ", Altitude: " + altitude + " }";
		} catch (JSONException e) {
			System.out.println(e.getMessage());
			return null;
		}
		return returnVal;
	}
}