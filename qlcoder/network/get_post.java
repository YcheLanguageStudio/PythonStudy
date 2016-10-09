import java.io.*;
import java.net.*;

class MainClass{
  public static void main(String[] args) throws IOException {
      String urlStr = "http://www.qlcoder.com/task/4/solve";
      URL url = new URL(urlStr);
      URLConnection conn = url.openConnection();
      conn.setRequestProperty("Accept", "application/json, text/javascript, */*; q=0.01");
      conn.setRequestProperty("Accept-Encoding", "gzip, deflate, sdch");
      conn.setRequestProperty("Accept-Language", "zh-CN,zh;q=0.8");
      conn.setRequestProperty("Connection", "keep-alive");
      conn.setRequestProperty("Cookie", "gr_user_id=4b052c27-6572-469c-ae84-fa12593fb787; remember_82e5d2c56bdd0811318f0cf078b78bfc=eyJpdiI6InA5TzVvVGVIRWJ1OFJ4Uk9BXC9JR0pnPT0iLCJ2YWx1ZSI6Ik1HM2VPWGN0dUQ3N3ZHMmlKXC9MZGpkU3Y1TFErZFhydDhvb1JINUVSVno1Q3c3OElOSDl1ZFpVNlwvNFI1NGVqUzZWdGJITWxhczZMUzdlYnR3UVI0bE1SY3duMlIxaWVRK3laZnVhWko1NHc9IiwibWFjIjoiZTczYzEwYTk0ODRmOTc4YzcxYTQ0MGQzMmFlNGEyMTBiNzAwOTEzYzQ2MGE0NzUwYzJjZjA3Y2ZiYjdkYzI1YSJ9; uuid=57f9a08614b8f; è¿é¢çç­æ¡æ¯oreo=eyJpdiI6InhwSjR2dTQ3aVduUTRJMCtQcitnY2c9PSIsInZhbHVlIjoiTHVwTVlPSWJcL21tcTg2QTJXSjNPc0E9PSIsIm1hYyI6ImNjMmM5YmE0ZTg5MWQwZDRkNzU5MzRiNGQ0MWQ1YjRmOTNlMjM1NjdkYmYyMWUwZmRmMjI1ZWZiMGEyYzM2NzgifQ%3D%3D; XSRF-TOKEN=eyJpdiI6ImcwOWFmQXM3SmhvZ3FqZVVURUVhQXc9PSIsInZhbHVlIjoiQkJudkVZUzZIeGlyMExTdWFPWFRzelBDQWR2bWZzZkxYZmNKVEJDNWpaN2crcDVuUU5oaXpFd2ZuSHBrQzFLQnozZlwvMFFENjdEQlJFZDk4R2pEU0NnPT0iLCJtYWMiOiJjNTcwM2I0OTYwN2Q3OTc3YTU0NDAzOTQ1OGNmOGQzYjk4MDBhNDQ0ZjIzNjdiNjExYjJmMjQxYTAxZjZmYjNiIn0%3D; laravel_session=eyJpdiI6IlF5a0NzUEdEa1RJXC8xdHhGVDlFQjNBPT0iLCJ2YWx1ZSI6InQyXC81YVd6T2pFc0N3ekhRejVlV0h2NmRkZ2x6ak5Zc25KNTMrQk9iWFZzY3hUY2pHWCs0Sml1T2lHNVZaVk03clZqbHhHaCtEU29GalhwRmZZMVRkZz09IiwibWFjIjoiODRjZTEwY2JiMzc5NTU0NzdkMDFkZmM0Mzc2ZTYyZTliMTFmMmE4MzgyZmMyYzJjMTI3MGYyZTliODE4YWU2ZiJ9; Hm_lvt_420590b976ac0a82d0b82a80985a3b8a=1475977341; Hm_lpvt_420590b976ac0a82d0b82a80985a3b8a=1475977395; gr_session_id_80dfd8ec4495dedb=852fcdf4-ed56-467d-aa97-745164383f07");
      conn.setDoOutput(true);
      PrintWriter pw = new PrintWriter(conn.getOutputStream());
      pw.print("answer=restful&_token=HGXNDUrh1yz2BPntbsfgUdFARjR05muG8OpCxn1B");
      pw.flush();
      BufferedReader reader = new BufferedReader(new InputStreamReader(conn.getInputStream()));
      String line = null;
      while((line = reader.readLine()) != null) {
          System.out.println(line);
      }
      reader.close();
  }
}
