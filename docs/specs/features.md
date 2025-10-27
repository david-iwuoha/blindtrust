# BlindTrust App - Features

## Main Features:
- **Account Creation**:  
  - Allow users to create an account with basic details such as name, phone number, and preferred language.  
  - Initial balance is seeded with ₦10,000 for demo purposes.

- **Balance Check**:  
  - Users can check their current balance via voice command. The app responds with the available balance in a clear, audible format.

- **Transaction History**:  
  - Users can view a list of their past transactions, with details such as date, amount, and recipient.  
  - Option to read transaction history in multiple languages (Pidgin, Igbo, Yoruba, etc.).

- **Add Beneficiary**:  
  - Users can add beneficiaries by speaking their name and account details. The app will store this information securely for future transactions.

- **Biometric Fallback**:  
  - For demo purposes, users can authenticate via biometric (fingerprint/face) or use a long-press simulation if their device doesn’t support biometric authentication.  
  - Biometric authentication is used for confirming transactions.

- **Modular Architecture**:  
  - All components (AI, speech recognition, transaction logic, etc.) are designed to be detachable and replaceable. This allows easy migration to production-level systems.

- **Multilingual Support**:  
  - The app supports multiple languages including English, Pidgin, Igbo, Yoruba, and Hausa. The user can switch languages based on preference.

- **Offline Mode**:  
  - If the device is offline, transactions can be queued and processed once the device reconnects to the internet.

## Voice Commands:
- “Check my balance” – Fetches the user’s current account balance.
- “Add a beneficiary” – Guides the user through the process of adding a new beneficiary.
- “Undo the last transaction” – Reverses the last transaction made by the user (if within the allowed time frame).
- “Switch language to [Language]” – Changes the language of the app’s voice interaction (e.g., “Switch language to Yoruba”).
- “Send [amount] to [beneficiary name]” – Initiates a transaction to a specified beneficiary.
- “Call my guardian” – Informs the user if their balance is too low and gives the option to call their guardian.
- “Show my transaction history” – Displays a list of recent transactions made by the user.
- “Set a reminder for my bills” – Allows users to schedule bill payments or reminders.

## User Experience (UX) Features:
- **Voice Feedback**:  
  - The app responds to every action with clear voice feedback, ensuring that visually impaired users know what’s happening at every stage (e.g., "Transfer successful, your new balance is ₦4,800").
  
- **Tactile Feedback**:  
  - The app provides haptic feedback, such as vibrations, when a transaction is successful or when an error occurs (e.g., insufficient funds).

- **Personalized Profiles**:  
  - Users can update their profile (name, preferred language, and profile picture).  
  - Users can choose an alias or nickname for the app to address them by (e.g., "Call me Emma").

- **Beneficiary List**:  
  - Users can manage their list of beneficiaries, which is securely stored locally or in the cloud depending on internet availability.
  
- **Error Handling**:  
  - If the system detects an issue (e.g., insufficient funds), it will suggest solutions, such as contacting a guardian or reattempting the transaction later.
  
- **Secure Transactions**:  
  - All transactions are secured through either biometric authentication or a PIN. The app ensures user data privacy is protected throughout.

## Business Features:
- **Demo-Only Mode**:  
  - The app is set to simulate transactions with fake money (₦10,000 initial balance), but the system is designed to easily integrate with real-world banking APIs when ready.

- **Real-Time Transaction Feedback**:  
  - Users receive instant updates about the status of their transactions. If a transfer is successful, the app provides the new balance and transaction ID.
  
- **Scalability**:  
  - The modular structure ensures that BlindTrust can easily scale to handle real-world transactions, additional language support, and integration with various financial institutions in the future.
