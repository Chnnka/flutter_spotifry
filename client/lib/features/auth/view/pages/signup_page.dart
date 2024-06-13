import 'package:client/core/theme/app_pallete.dart';
import 'package:client/features/auth/view/widgets/auth_button.dart';
import 'package:client/features/auth/view/widgets/custom_textfield.dart';
import 'package:flutter/material.dart';

class SignupPage extends StatefulWidget {
  const SignupPage({super.key});

  @override
  State<SignupPage> createState() => _SignupPageState();
}

class _SignupPageState extends State<SignupPage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Padding(
        padding: const EdgeInsets.symmetric(horizontal: 15),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const Text(
              'Sign Up ♪',
              style: TextStyle(
                fontSize: 50,
                fontWeight: FontWeight.bold,
              ),
            ),
            const SizedBox(height: 20),
            const CustomTextfield(
              hintText: 'Name',
              obscureText: false,
            ),
            const SizedBox(height: 10),
            const CustomTextfield(
              hintText: 'Email',
              obscureText: false,
            ),
            const SizedBox(height: 10),
            const CustomTextfield(
              hintText: 'Password',
              obscureText: true,
            ),
            const SizedBox(height: 20),
            const AuthButton(),
            const SizedBox(height: 20),
            RichText(
              text: const TextSpan(
                text: 'Already have an account?',
                children: [
                  TextSpan(
                    text: ' Sign In',
                    style: TextStyle(
                      color: Pallete.greenColor,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}
