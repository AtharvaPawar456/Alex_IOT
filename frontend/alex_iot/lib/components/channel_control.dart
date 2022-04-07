import 'package:alex_iot/services/channel_control.dart';
import 'package:flutter/material.dart';

class ChannelControl extends StatefulWidget {
  const ChannelControl({Key? key, this.temperature, this.humidity})
      : super(key: key);

  final humidity;
  final temperature;

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
                      setState(() {
                        switchStates[index] = state;
                      });
                      if (switchStates[index]) {
                        channels[index] += 50;
                        print(channels[index]);
                      } else {
                        channels[index] -= 50;
                        print(channels[index]);
                      }

                      updateChannel(
                          channels[index], widget.temperature, widget.humidity);
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
