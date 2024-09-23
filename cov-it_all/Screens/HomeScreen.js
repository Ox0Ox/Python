import * as React from 'react';
import { Text, View, StyleSheet,TouchableOpacity,TextInput,Alert,Image, ImageBackground } from 'react-native';
import AppHeader from '../components/AppHeader'
import firebase from 'firebase'
import db from '../config'
import LoginScreen from './LoginScreen'

export default class Home extends React.Component{
  LoginPage=()=>{
    //console.log("entering")
    this.props.navigation.navigate('LoginScreen')
  }
  render(){
    return(
      <View style = {styles.container}>
       <ImageBackground source={require('../assets/LG1.jpeg')} style={styles.image}>
        <Image style={{width:250,height:50,marginTop:0,}}source={require('../assets/COVIT2.png')}/>
        <View>
        <TouchableOpacity style={styles.button}
      onPress={()=>{this.LoginPage()}}>
      <Text style={styles.buttonText}>
        Login/Sign-Up 
      </Text>
      </TouchableOpacity>
      </View>
        </ImageBackground>
        
      </View>
    )
  }
}

const styles = StyleSheet.create({
   container: {
    flex: 1,
    width: '100%',
    height: '100%',
    alignSelf: 'center',
    justifyContent: "center",
    alignItems: "center",
    
  },

   buttonText:{
    alignSelf: 'center',
    width:200,
    height:40,
    marginTop:10,
    textAlign:'center',
    fontSize:25,
    fontWeight: 'bold',
    //alignSelf: 'center',
    borderRadius:10,
    //borderColor:'blue',
    //backgroundColor:'cyan',
    color:'aqua'
  },
   button:{
    alignSelf: 'center',
    //alignItems:'çenter',
    justifyContent:'center',
    width:200,
    height:60,
    marginTop:250,
    borderRadius:20,
    borderWidth:2,
    borderColor: "white",
    backgroundColor:'transparent',
  },
  image:{
   //position:'absolute',
    //marginTop:50,
    flex: 1,
    width: '100%',
    height: '100%',
    alignSelf: 'center',
    justifyContent: "center",
    alignItems: "center",
    //opacity: 0.7,
    //backgroundColor: 'red'

  },
   paragraph: {
    //position:'relative',
    //top:'20%',
    marginTop: 0,
    fontSize: 18,
    fontWeight: 'bold',
    alignSelf: 'center',
    fontFamily: 'fenice',
    color:'white',
  },
  para:{
    textAlign: 'center',
    fontWeight: 'bold',
    fontFamily: 'helvetica'
  }
})