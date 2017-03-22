
class Filter {
	public static void main(String[] args) {
		//json objects are assumed to be sanitised
		String JSONString1 = "{ ID: '135875', Longitude: 28.2247, Latitude: -25.7521, Altitude: 2435 }"; //test case 1 (should be in bounds)
		String JSONString2 = "{ ID: '425478', Longitude: 28.223, Latitude: -25.7125, Altitude: 152 }"; //test case 2 (should be out of bounds)
		
		JSONObject jsonObject1 = new JSONObject(JSONString1) ;
		JSONObject jsonObject2 = new JSONObject(JSONString2) ;
		
		System.out.println("Filtering test case 1") ;
		
		if (validJSONString(jsonObject1)) 
			System.out.println("Object with ID: [" + obj.getString("ID") + "] is valid") ;
		else 
			System.out.println("ERROR: Object with ID: [" + obj.getString("ID") + "] is invalid") ;
		
		
		System.out.println("-----------------------------------");

		
		System.out.println("Filtering test case 2") ;
		
		if (validJSONString(jsonObject2)) 
			System.out.println("Object with ID: [" + obj.getString("ID") + "] is valid") ;
		else 
			System.out.println("ERROR: Object with ID: [" + obj.getString("ID") + "] is invalid") ;
		
		
		System.out.println("End Test");
		
	}

	
	static boolean validJSONString(JSONObject obj) {
		//upper and lower limits for latitide/longitude
		//I'm assuming we are using decimal representation of coordinates
		//These limits are rough estimates obtained from google maps, but they should suffice for now
		//I'm unsure of the altitude units or bounds
		double altUpperLimit = 3000 ;
		double altLowerLimit = -3000 ;
		double longUpperLimit = 28.237 ;
		double longLowerLimit = 28.225 ;
		double latUpperLimit = -25.75 ;
		double latLowerLimit =  -25.7575 ;
		
		try {
			double latitude = obj.getDouble("Latitude") ;
			double longitude = obj.getDouble("Longitude") ;
			double altitude = obj.getDouble("Altitude") ;
		
		
			if (latitude > latUpperLimit || latitude < latLowerLimit) //check latitude bounds
				return false ;
		
			if (longitude > longUpperLimit || longitude < longLowerLimit) //check longitude bounds
				return false ;
		
			if (altitude > altUpperLimit || altitude < altLowerLimit) //check altitude bounds
				return false ;
		
			return true ;
		}
		catch(JSONException e) {
			System.out.println("EXCEPTION: Error when parsing coordinates") ;
			return false ;
		}
	}
}