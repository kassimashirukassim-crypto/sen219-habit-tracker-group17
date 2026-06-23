import 'package:flutter/material.dart';

void main() {
  runApp(const Group17HabitTrackerApp());
}

class Group17HabitTrackerApp extends StatelessWidget {
  const Group17HabitTrackerApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Group 17 Habit Tracker',
      theme: ThemeData(
        useMaterial3: true,
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.teal, brightness: Brightness.dark),
      ),
      home: const MobileTrackerHome(),
      debugShowCheckedModeBanner: false,
    );
  }
}

class MobileTrackerHome extends StatefulWidget {
  const MobileTrackerHome({Key? key}) : super(key: key);

  @override
  _MobileTrackerHomeState createState() => _MobileTrackerHomeState();
}

class _MobileTrackerHomeState extends State<MobileTrackerHome> {
  final Map<String, List<bool>> _studentHabits = {
    "Study for SEN 219": [false, false, false, false, false, false, false],
    "Review Exam Timetable": [false, false, false, false, false, false, false],
    "Drink 3L of Water": [false, false, false, false, false, false, false],
    "Sleep 7+ Hours": [false, false, false, false, false, false, false],
  };

  final List<String> _weekDays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"];
  final TextEditingController _inputController = TextEditingController();

  double _getWeeklyScore() {
    int totalSlots = _studentHabits.length * 7;
    int itemsCompleted = 0;
    _studentHabits.forEach((habit, checkedList) {
      itemsCompleted += checkedList.where((element) => element == true).length;
    });
    return totalSlots > 0 ? (itemsCompleted / totalSlots) * 100 : 0.0;
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("SEN 219 — Group 17 Tracker"),
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        centerTitle: true,
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            Card(
              color: Theme.of(context).colorScheme.primaryContainer,
              child: Padding(
                padding: const EdgeInsets.all(16.0),
                child: Column(
                  children: [
                    const Text("📊 Overall Performance Metrics", style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold)),
                    const SizedBox(height: 5),
                    Text("${_getWeeklyScore().toStringAsFixed(1)}% Efficiency", style: const TextStyle(fontSize: 24, fontWeight: FontWeight.bold, color: Colors.greenAccent)),
                  ],
                ),
              ),
            ),
            const SizedBox(height: 15),
            Expanded(
              child: ListView(
                children: _studentHabits.keys.map((String habitName) {
                  return Card(
                    child: Padding(
                      padding: const EdgeInsets.symmetric(vertical: 10.0, horizontal: 14.0),
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Text(habitName, style: const TextStyle(fontSize: 14, fontWeight: FontWeight.bold)),
                          const SizedBox(height: 8),
                          Row(
                            mainAxisAlignment: MainAxisAlignment.spaceBetween,
                            children: List.generate(7, (index) {
                              return Column(
                                children: [
                                  Text(_weekDays[index], style: const TextStyle(fontSize: 10, color: Colors.grey)),
                                  Checkbox(
                                    value: _studentHabits[habitName]![index],
                                    onChanged: (bool? newValue) {
                                      setState(() {
                                        _studentHabits[habitName]![index] = newValue ?? false;
                                      });
                                    },
                                  ),
                                ],
                              );
                            }),
                          )
                        ],
                      ),
                    ),
                  );
                }).toList(),
              ),
            ),
            Row(
              children: [
                Expanded(
                  child: TextField(
                    controller: _inputController,
                    decoration: const InputDecoration(labelText: 'Add Custom Mobile Habit...'),
                  ),
                ),
                IconButton(
                  icon: const Icon(Icons.add_circle, color: Colors.teal),
                  onPressed: () {
                    if (_inputController.text.trim().isNotEmpty) {
                      setState(() {
                        _studentHabits[_inputController.text.trim()] = [false, false, false, false, false, false, false];
                        _inputController.clear();
                      });
                    }
                  },
                )
              ],
            ),
          ],
        ),
      ),
    );
  }
}
