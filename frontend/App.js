import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';

import LoginScreen from './src/screens/LoginScreen';
// import CadastroScreen from './src/screens/CadastroScreen';
// import EsqueciSenhaScreen from './src/screens/EsqueciSenhaScreen';

const Stack = createNativeStackNavigator();

export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Login">
        <Stack.Screen
          name="Login"
          component={LoginScreen}
          options={{ title: 'Bem-vindo' }}
        />
        {/* <Stack.Screen name="Cadastro" component={CadastroScreen} /> */}
        {/* <Stack.Screen name="EsqueciSenha" component={EsqueciSenhaScreen} /> */}
      </Stack.Navigator>
    </NavigationContainer>
  );
}
