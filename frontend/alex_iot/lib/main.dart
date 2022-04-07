import 'package:alex_iot/models/thing_speak.dart';
import 'package:alex_iot/services/thing_speak.dart';
import 'package:flutter/material.dart';

import 'components/channel_control.dart';
import 'components/temp_hum_widget.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Alex IOT',
      theme: ThemeData(
        brightness: Brightness.dark,
        primarySwatch: Colors.deepOrange,
      ),
      home: const LoginPage(),
    );
  }
}

class LoginPage extends StatelessWidget {
  const LoginPage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
      title: const Text("Login"),
    ));
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({Key? key, required this.title}) : super(key: key);

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Alex IOT"),
        backgroundColor: Colors.deepOrange,
      ),
      body: Center(
        child: Padding(
          padding: const EdgeInsets.all(10.0),
          child: ListView(
            children: <Widget>[
              FutureBuilder<ThingSpeak>(
                  future: getThingSpeakData(),
                  builder: (context, snapshot) {
                    if (snapshot.hasData) {
                      final temperature = snapshot.data?.feeds[0].field2;
                      final humidity = snapshot.data?.feeds[0].field3;

                      return Padding(
                        padding: const EdgeInsets.all(20.0),
                        child: Column(
                          children: [
                            TempHumWidget(
                              temperature: temperature,
                              humidity: humidity,
                            ),
                            const SizedBox(height: 50),
                            ChannelControl(
                                temperature: temperature, humidity: humidity)
                          ],
                        ),
                      );
                    } else if (snapshot.hasError) {
                      return Text("${snapshot.error}");
                    }
                    return const Center(child: CircularProgressIndicator());
                  })
            ],
          ),
        ),
      ),
    );
  }
}
