// ignore_for_file: prefer_typing_uninitialized_variables

import 'package:alex_iot/services/channel_control.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';

class ChannelControl extends StatefulWidget {
  const ChannelControl({Key? key, this.temperature, this.humidity, this.user})
      : super(key: key);

  final humidity;
  final temperature;
  final user;

  @override
  State<ChannelControl> createState() => _ChannelControlState();
}

class _ChannelControlState extends State<ChannelControl> {
  final List<String> names = [
    "Channel 1",
    "Channel 2",
    "Channel 3",
    "Channel 4"
  ];
  final List<int> channels = [400, 500, 600, 700];
  final List<bool> switchStates = [false, false, false, false];

  @override
  Widget build(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.stretch,
      children: [
        const Text(
          "Channel Control",
          style: TextStyle(
            color: Colors.grey,
          ),
        ),
        const SizedBox(height: 10),
        ListView.builder(
          shrinkWrap: true,
          itemCount: channels.length,
          itemBuilder: (context, index) {
            return Padding(
              padding: const EdgeInsets.only(bottom: 10),
              child: Row(
                children: [
                  Expanded(child: Text(names[index])),
                  IconButton(
                    iconSize: 20,
                    onPressed: () {},
                    icon: const Icon(Icons.edit),
                  ),
                  const SizedBox(height: 10),
                  Switch(
                    value: switchStates[index],
                    onChanged: (state) {
                      final temp;

                      if (switchStates[index]) {
                        temp = channels[index] - 50;
                      } else {
                        temp = channels[index] + 50;
                      }

                      updateChannel(
                        widget.user.uid,
                        temp,
                        widget.temperature,
                        widget.humidity,
                      ).then((value) {
                        setState(() {
                          if (value != "0") {
                            channels[index] = temp;
                            switchStates[index] = state;
                          } else {
                            ScaffoldMessenger.of(context)
                                .showSnackBar(const SnackBar(
                              content: Text("Updating Failed ..."),
                            ));
                          }
                        });
                      });
                    },
                  ),
                  Text("${channels[index]}"),
                ],
              ),
            );
          },
        ),
      ],
    );
  }
}
