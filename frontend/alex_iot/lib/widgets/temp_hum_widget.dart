// ignore_for_file: prefer_typing_uninitialized_variables

import 'package:flutter/material.dart';

class TempHumWidget extends StatelessWidget {
  const TempHumWidget({
    Key? key,
    required this.temperature,
    required this.humidity,
  }) : super(key: key);

  final humidity;
  final temperature;

  @override
  Widget build(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.stretch,
      children: [
        const Text(
          "Climate",
          style: TextStyle(
            color: Colors.grey,
          ),
        ),
        const SizedBox(height: 10),
        TempHumCard(
          title: "Temperature",
          value:
              temperature.toString() == "null" ? "N/A" : temperature.toString(),
        ),
        TempHumCard(
          title: "Humidity",
          value: humidity.toString() == "null" ? "N/A" : humidity.toString(),
        )
      ],
    );
  }
}

class TempHumCard extends StatelessWidget {
  const TempHumCard({
    Key? key,
    required this.title,
    required this.value,
  }) : super(key: key);

  final String title;
  final String value;

  @override
  Widget build(BuildContext context) {
    return Card(
      clipBehavior: Clip.antiAlias,
      child: Padding(
        padding: const EdgeInsets.all(15.0),
        child: Column(
          children: [
            Text(
              title,
              style: const TextStyle(
                color: Colors.grey,
              ),
            ),
            const SizedBox(height: 10),
            Text(
              value,
              style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 20),
            ),
          ],
        ),
      ),
    );
  }
}
