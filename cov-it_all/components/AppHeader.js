import * as React from 'react';
import { Text, View, StyleSheet, Image } from 'react-native';
//import { SafeAreaProvider} from 'react-native-safe-area-context';
import{Header} from 'react-native-elements'



export default class AppHeader extends React.Component {
  render(){
  return (
    <View style={styles.container}>
    <Text style={styles.paragraph}>
        COV-IT ALL  
      </Text>
    <View>
     <Image style={{width:70,height:70,marginTop:0,}}source={require('../assets/LOGO.jpeg')}/>
    </View>
    </View>
  );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    marginTop:10,
    backgroundColor: 'aqua',
    padding: 8,
  },
  paragraph: {
    //marginLeft: 50,
    marginTop: 10,
    fontSize: 18,
    fontWeight: 'bold',
    textAlign: 'center',
  },
});
