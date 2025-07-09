import 'package:flutter/material.dart';
import 'package:shopify/core/theme/theme.dart';
import 'package:shopify/features/auth_feature/view/pages/signup_page.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: AppTheme.darkThemeMode,

      home: SignupPage(),
    );
  }
}
