import 'package:alex_iot/firebase/auth.dart';
import 'package:alex_iot/models/thing_speak.dart';
import 'package:alex_iot/services/thing_speak.dart';
import 'package:alex_iot/widgets/channel_control.dart';
import 'package:alex_iot/widgets/google_sign_in_btn.dart';
import 'package:alex_iot/widgets/temp_hum_widget.dart';
import 'package:flutter/material.dart';

class LoginPage extends StatelessWidget {
  const LoginPage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        body: Center(
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: const [
              Text(
                "Sign",
                style: TextStyle(
                  fontSize: 30,
                  fontWeight: FontWeight.bold,
                ),
              ),
              Text(
                " In",
                style: TextStyle(
                  color: Colors.deepOrange,
                  fontSize: 30,
                  fontWeight: FontWeight.bold,
                ),
              ),
            ],
          ),
          const SizedBox(height: 30),
          FutureBuilder(
            future: Auth.initializeFirebase(context: context),
            builder: (context, snapshot) {
              if (snapshot.hasError) {
                // print(snapshot.error);
                return const Text('Error initializing Firebase');
              } else if (snapshot.connectionState == ConnectionState.done) {
                return const GoogleSignInButton();
              }
              return const CircularProgressIndicator(
                valueColor: AlwaysStoppedAnimation<Color>(
                  Colors.deepOrange,
                ),
              );
            },
          ),
        ],
      ),
    ));
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({Key? key}) : super(key: key);

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
