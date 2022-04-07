import 'package:alex_iot/firebase/auth.dart';
import 'package:alex_iot/widgets/google_sign_in_btn.dart';
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
