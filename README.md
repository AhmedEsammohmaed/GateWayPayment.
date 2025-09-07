# 🌐 Gateway CLI Project  

_A Python-based **API Gateway simulation** built with **OOP, SOLID principles, and Clean Architecture**. Designed as a console project to demonstrate **system design concepts, payment routing, authentication, and modular microservices**._  

![Build](https://img.shields.io/badge/build-passing-brightgreen)  
![Python](https://img.shields.io/badge/python-3.9%2B-blue)  
![License](https://img.shields.io/badge/license-MIT-lightgrey)  
![Coverage](https://img.shields.io/badge/tests-95%25-success)  

---

## 📖 Overview
This project simulates a **Payment Gateway System** where users can:  
- Authenticate with a secure password  
- Transfer money between accounts  
- Use **Visa** or **Wallet** for payments  
- Persist user balances with file storage  

The system is designed with **FAANG-level coding standards**:  
- **OOP Inheritance**: `User`, `Visa`, and `Wallet`  
- **Encapsulation & Polymorphism**: Overridden methods for different payment types  
- **SOLID Principles**: Separation of concerns across modules  
- **Persistence Layer**: Save/load balances via serialization  
- **Scalable Architecture**: Easy to extend with new payment methods  

---

## 🚀 Features
- ✅ **User Authentication** with password validation  
- ✅ **Balance Management** (add, deduct, transfer)  
- ✅ **Visa & Wallet Integration** with custom behavior  
- ✅ **Data Persistence** using file serialization (`pickle`)  
- ✅ **Transaction Logging** for transparency  
- ✅ **Extensible Architecture** (add new payment providers easily)  
- ✅ **Unit Tests** for robustness  

---

## 📂 Project Structure
