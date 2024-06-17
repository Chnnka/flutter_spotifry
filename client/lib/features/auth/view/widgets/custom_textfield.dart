import 'package:flutter/material.dart';

class CustomTextfield extends StatelessWidget {
  final bool obscureText;
  final String hintText;
  final TextEditingController controller;
  const CustomTextfield(
      {super.key,
      this.obscureText = false,
      required this.hintText,
      required this.controller});

  @override
  Widget build(BuildContext context) {
    return TextFormField(
      controller: controller,
      obscureText: obscureText,
      decoration: InputDecoration(hintText: hintText),
    );
  }
}
