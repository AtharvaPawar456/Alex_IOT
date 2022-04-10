import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:http/http.dart' as http;

Future<String> updateChannel(uid, value, temperature, humidity) async {
  // final channelNo = (value / 100) - 3;
  var doc =
      await FirebaseFirestore.instance.collection('apiKeys').doc(uid).get();
  String url =
      "https://api.thingspeak.com/update?api_key=${doc['apiKey']}&field1=$value&field2=$temperature&field3=$humidity";
  final response = await http.get(Uri.parse(url));
  return response.body;
}
