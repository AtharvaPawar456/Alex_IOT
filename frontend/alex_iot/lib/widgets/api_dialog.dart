import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';

Future<void> showInformationDialog(BuildContext context, User? user) async {
  final GlobalKey<FormState> _formKey = GlobalKey<FormState>();

  final TextEditingController _textEditingController = TextEditingController();

  return await showDialog(
      context: context,
      builder: (context) {
        return StatefulBuilder(builder: (context, setState) {
          return AlertDialog(
            content: Form(
                key: _formKey,
                child: Column(
                  mainAxisSize: MainAxisSize.min,
                  children: [
                    TextFormField(
                      controller: _textEditingController,
                      validator: (value) {
                        return value!.isNotEmpty ? null : "Enter any text";
                      },
                      decoration: const InputDecoration(hintText: "API Key"),
                    ),
                  ],
                )),
            title: const Text('Thing Speak API Key'),
            actions: <Widget>[
              InkWell(
                child: const Text('OK   '),
                onTap: () {
                  if (_formKey.currentState!.validate()) {
                    // Do something like updating SharedPreferences or User Settings etc.
                    // FirebaseFirestore.instance.collection('user').doc().set(
                    //     <String, dynamic>{"name": _textEditingController.text});
                    if (user != null) {
                      FirebaseFirestore.instance
                          .collection('apiKeys')
                          .doc(user.uid)
                          .set(
                        <String, dynamic>{
                          "apiKey": _textEditingController.text
                        },
                        SetOptions(merge: true),
                      ).catchError((e) => {
                                ScaffoldMessenger.of(context)
                                    .showSnackBar(SnackBar(
                                  content: Text(e),
                                ))
                              });
                    } else {
                      if (kDebugMode) {
                        print("User does not exist created");
                      }
                    }

                    Navigator.of(context).pop();
                  }
                },
              ),
            ],
          );
        });
      });
}
