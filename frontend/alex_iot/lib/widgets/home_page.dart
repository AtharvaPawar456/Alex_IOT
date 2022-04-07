import 'package:alex_iot/firebase/auth.dart';
import 'package:alex_iot/models/thing_speak.dart';
import 'package:alex_iot/services/thing_speak.dart';
import 'package:alex_iot/widgets/channel_control.dart';
import 'package:alex_iot/widgets/login.dart';
import 'package:alex_iot/widgets/temp_hum_widget.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';

class MyHomePage extends StatefulWidget {
  const MyHomePage({Key? key, this.user}) : super(key: key);

  final User? user;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Alex IOT"),
        actions: [
          if (widget.user != null && widget.user!.photoURL != null)
            Padding(
              padding: const EdgeInsets.all(10.0),
              child: CircleAvatar(
                backgroundImage: NetworkImage(widget.user!.photoURL as String),
              ),
            )
          else
            const Padding(
              padding: EdgeInsets.all(10.0),
              child: Icon(Icons.account_circle),
            ),
          IconButton(
              onPressed: () {
                Auth.signOut(context: context);
                Navigator.of(context).pushReplacement(
                  MaterialPageRoute(
                    builder: (context) => const LoginPage(),
                  ),
                );
              },
              icon: const Icon(Icons.exit_to_app))
        ],
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
