import * as React from 'react';
import { Text, View, StyleSheet } from 'react-native';
import {createSwitchNavigator,createAppContainer} from 'react-navigation'
import AppHeader from './components/AppHeader'
import MustKnowScreen from './Screens/MustKnow'
import MainScreen from './Screens/mainScreen'
import Covid from './Screens/Covid'
import Laugh from './Screens/Laugh'
import LoginScreen from './Screens/LoginScreen'
import HomeScreen from './Screens/HomeScreen'
import Aware from './Screens/Aware'
import Myth from './Screens/Myth'
import Norm from './Screens/NormQ'

export default function App() {
  return (
    <View style = {styles.container}>
      <AppContainer/>    
    </View>
  );
}
const SwtichNavigator=createSwitchNavigator({
  HomeScreen:HomeScreen,
  LoginScreen:LoginScreen,
  MainScreen:MainScreen,
  MustKnowScreen:MustKnowScreen,
  Laugh:Laugh,
  Aware:Aware,
  Covid:Covid,
  Myth:Myth,
  Norm:Norm,
});
const AppContainer= createAppContainer(SwtichNavigator);

const styles = StyleSheet.create({
  container: {
    flex: 1,
    //justifyContent: 'center',
  },
  paragraph: {
    margin: 24,
    fontSize: 18,
    fontWeight: 'bold',
    textAlign: 'center',
  },
});
