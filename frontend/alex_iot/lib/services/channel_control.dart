import 'package:http/http.dart' as http;

Future<String> updateChannel(value, temperature, humidity) async {
  // final channelNo = (value / 100) - 3;

  String url =
      "https://api.thingspeak.com/update?api_key=YYN5LAINXD8Y6Y4A&field1=$value&field2=$temperature&field3=$humidity";
  final response = await http.get(Uri.parse(url));
  return response.body;
}
