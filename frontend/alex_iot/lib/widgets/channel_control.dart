// ignore_for_file: prefer_typing_uninitialized_variables

import 'package:alex_iot/services/channel_control.dart';
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
  final List<int> channels = [450, 550, 650, 750];
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
                      var temp, prev;

                      if (switchStates[index]) {
                        temp = channels[index] + 50;
                      } else {
                        temp = channels[index] - 50;
                      }

                      setState(() {
                        prev = channels[index];
                        channels[index] = temp;
                        switchStates[index] = state;
                      });

                      updateChannel(
                        widget.user.uid,
                        channels[index],
                        widget.temperature,
                        widget.humidity,
                      ).then((value) {
                        setState(() {
                          if (value == "0") {
                            channels[index] = prev;
                            switchStates[index] = !state;
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
