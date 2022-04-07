import 'package:firebase_core/firebase_core.dart';

Future<FirebaseApp> _initializeFirebase() async {
  FirebaseApp app = await Firebase.initializeApp();
  return app;
}
