import 'dart:convert';

import 'package:alex_iot/models/thing_speak.dart';
import 'package:http/http.dart' as http;

String url =
    "https://api.thingspeak.com/channels/1661789/feeds.json?api_key=BWRV718JS99HRK3N";

Future<ThingSpeak> getThingSpeakData() async {
  final response = await http.get(Uri.parse("$url&results=1"));
  return ThingSpeak.fromJson(json.decode(response.body));
}
