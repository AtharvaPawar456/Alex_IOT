import 'dart:convert';

import 'package:alex_iot/models/thing_speak.dart';
import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:http/http.dart' as http;

Future<ThingSpeak> getThingSpeakData(String uid) async {
  // Sample : YYN5LAINXD8Y6Y4A
  var doc =
      await FirebaseFirestore.instance.collection('apiKeys').doc(uid).get();

  final response = await http.get(Uri.parse(
      "https://api.thingspeak.com/channels/1661789/feeds.json?api_key=${doc['apiKey']}&results=1"));

  return ThingSpeak.fromJson(json.decode(response.body));
}
