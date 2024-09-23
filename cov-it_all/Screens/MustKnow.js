import * as React from 'react';
import { Text, View, StyleSheet,TouchableOpacity,Image, ImageBackground } from 'react-native';
import firebase from 'firebase';
import db from '../config';


export default class MustKnowScreen extends React.Component {
  render(){
  return (
    <View >
    <ImageBackground source={require('../assets/Must.png')} style={{alignSelf:'center', width:'100%' ,height:'100%'}}>
     <TouchableOpacity 
      onPress={()=>{this.props.navigation.navigate("MainScreen")}}>
      <Image style={{width:280,height:50, alignSelf: 'center', marginTop: 50}}source={require('../assets/COV.png')}/>
      </TouchableOpacity>
      <Text style={styles.paragraph}>
      Must Know During the COVID Era 
      </Text>
      <TouchableOpacity onPress={()=>{this.props.navigation.navigate("MainScreen")}}>
      <Image style={{width:30,height:30, alignSelf: 'left', marginTop: 0, marginLeft:5,}}source={require('../assets/Backbutton.png')}/>
      </TouchableOpacity>
      <View style = {{marginTop:20, marginLeft:15,}}>
      <Text style={{fontSize:24,fontWeight: 'bold',fontFamily:'couriernew'}}>
      COVID essentials-
      </Text>
      <Text style={styles.para}>
      -Sanitizer
      </Text>
      <Text style={styles.para}>
      -Mask
      </Text>
      <Text style={styles.para}>
      -Face shield
      </Text>
      <Text style={styles.para}>
      -Cleansers
      </Text>
      <Text style={styles.para}>
      -Gloves
      </Text>
      <Text style={styles.para}>
      -Disinfectants
      </Text>
      <Text style={styles.para}>
      -Oximeters
      </Text>
    </View>
    <View style = {{marginTop:20, marginLeft:15,}}>
      <Text style={{fontSize:24,fontWeight: 'bold',fontFamily:'couriernew'}}>
      Do's-
      </Text>
      <Text style={styles.para}>
      -Drink a lot of water
      </Text>
      <Text style={styles.para}>
      -Eat a well-balanced diet
      </Text>
      <Text style={styles.para}>
      -Do some light exercise/physical activity
      </Text>
      <Text style={styles.para}>
      -Wear a mask at all times and try wearing a double mask
      </Text>
      <Text style={styles.para}>
      -Get at least 7 to 8 hours of sleep
      </Text>
      <Text style={styles.para}>
      -Maintain social distancing of 6 feet at all times
      </Text>
    </View>
    <View style = {{marginTop:20, marginLeft:15,}}>
      <Text style={{fontSize:24,fontWeight: 'bold',fontFamily:'couriernew'}}>
      Dont's-
      </Text>
      <Text style={styles.para}>
      -Consume alcohol and tobacco
      </Text>
      <Text style={styles.para}>
      -Think that you are completely immune to COVID-19 after vaccination
      </Text>
      <Text style={styles.para}>
      -Delay consulting a doctor if you experience COVID-19 symptoms even after vaccination
      </Text>
      <Text style={styles.para}>
      -Go out frequently after receiving your vaccines
      </Text>
      <Text style={styles.para}>
      -Get at least 7 to 8 hours of sleep
      </Text>
    </View>
    </ImageBackground>
    </View>
  );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 0.1,
    justifyContent: 'center',
    
    backgroundColor: 'aqua',
    padding: 8,
  },
  button:{
    marginLeft:70,
    width:200,
    height:80,
    marginTop:100,
    borderRadius:20,
    backgroundColor:'red'
  },
  paragraph: {
    margin: 26,
    fontSize: 30,
    fontWeight: 'bold',
    textAlign: 'center',
    fontStyle: 'italic'
    //backgroundColor:'red'
  },
  para: {
    margin: 0,
    fontSize: 18,
    fontWeight: 'bold',
    textAlign: 'left',
    fontFamily:'couriernew'
  },
});
