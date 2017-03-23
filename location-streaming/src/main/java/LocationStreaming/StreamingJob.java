package LocationStreaming;


import org.apache.flink.api.common.functions.FilterFunction;
import org.json.JSONException;
import org.json.JSONObject;
import org.apache.flink.api.common.functions.MapFunction;
import org.apache.flink.core.fs.FileSystem.WriteMode;
import org.apache.flink.streaming.api.datastream.DataStream;
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;


/**
 * Skeleton for a Flink Streaming Job.
 *
 * For a full example of a Flink Streaming Job, see the SocketTextStreamWordCount.java
 * file in the same package/directory or have a look at the website.
 *
 * You can also generate a .jar file that you can submit on your Flink
 * cluster.
 * Just type
 * 		mvn clean package
 * in the projects root directory.
 * You will find the jar in
 * 		target/location-streaming-0.1.jar
 * From the CLI you can then run
 * 		./bin/flink run -c LocationStreaming.StreamingJob target/location-streaming-0.1.jar
 *
 * For more information on the CLI see:
 *
 * http://flink.apache.org/docs/latest/apis/cli.html
 */
public class StreamingJob {

	public static void main(String[] args) throws Exception {
		// set up the streaming execution environment
	 // TODO code application logic here
      		final  StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();
        	DataStream<String > inputStream=env.socketTextStream("localhost", 2001);
 			 inputStream.map(new Sanitize()).filter(new Filter()).writeAsText("/home/seonin/output.txt", WriteMode.OVERWRITE);
   			 env.execute("Location Streaming");
	}
	 public static class Sanitize implements MapFunction<String, String>
    {
            @Override
            public String map(String _json) throws Exception {
            String returnVal = "Error";
		try {
			//If any variable names change then just change the strings inside the get functions parameter
			JSONObject jsonObject = new JSONObject(_json);
                        int userID = jsonObject.getInt("ID");
		

			double longitude = jsonObject.getDouble("longitude");
		

			double latitude = jsonObject.getDouble("latitude");
			

			double altitude = jsonObject.getDouble("altitude");
			

			returnVal = "{ \"ID\": '" + userID + "', \"Longitude\": " + longitude + ", \"Latitude\": " + latitude + ", \"Altitude\": " + altitude + " }";
		} catch (JSONException e) {
			System.out.println(e.getMessage());
			return null;
		}
		return returnVal;
    }
            
  }
     
public static class Filter implements FilterFunction<String>{
                    @Override
                    public boolean filter(String value)  throws Exception{
                        JSONObject obj = new JSONObject(value);    
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
		
		
                                if (latitude < -90.00 || latitude > 90.0) //check latitude bounds
                                        return false ;
		
                                if (longitude < -180.0 || longitude >180) //check longitude bounds
                                        return false ;
                            //check altitude bounds
                            		
                                return altitude <= 4000 ;
                            }
                            catch(JSONException e) {
                                    System.out.println("EXCEPTION: Error when parsing coordinates") ;
                                    return false ;
                                 }
		
                    }
                }
}
