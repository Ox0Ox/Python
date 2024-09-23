import * as React from 'react';
import { Text, View, StyleSheet,TouchableOpacity,TextInput, Image, ImageBackground } from 'react-native';
import AppHeader from '../components/AppHeader'
import MustKnow from './MustKnow'
import firebase from 'firebase'
//import Speaker from "expo-speaker"



export default class MainScreen extends React.Component {
  constructor(){
    super()
    this.state={
      text:""
    }
  }
  mustPage=()=>{
    //console.log("entering")
    this.props.navigation.navigate('MustKnowScreen')
  }
   covidPage=()=>{
    //console.log("entering")
    this.props.navigation.navigate('Covid')
  }
  laughPage=()=>{
    //console.log("entering")
    this.props.navigation.navigate('Laugh')
  }
  awarePage=()=>{
    //console.log("entering")
    this.props.navigation.navigate('Aware')
  }
  mythPage=()=>{
    //console.log("entering")
    this.props.navigation.navigate('Myth')
  }
  render(){
  return (
    <View style = {styles.container} >
    <ImageBackground source={require('../assets/Must.png')} style={{alignSelf:'center', width:'100%' ,height:'100%'}}>
   <TouchableOpacity 
      onPress={()=>{this.props.navigation.navigate("MainScreen")}}>
      <Image style={{width:280,height:50, alignSelf: 'center', marginTop: 50}}source={require('../assets/COV.png')}/>
      </TouchableOpacity>
     <TouchableOpacity style ={{marginLeft:270}}
    onPress={()=>{
      this.props.navigation.navigate('HomeScreen')
      firebase.auth().signOut()
    }}>
    <Image style={{width:40,height:40, alignSelf: 'center', marginTop: 50}}source={require('../assets/Logout.png')}/>
    </TouchableOpacity>
    <TouchableOpacity style={styles.button}
    onPress={()=>{this.covidPage()}}>
    <Text style={styles.para}>
      Covid Count in India 
    </Text>
    </TouchableOpacity>
    <TouchableOpacity style={styles.button}
    onPress={()=>{this.mustPage()}}>
    <Text style={styles.paragraph}>
      Must Know
    </Text>
    </TouchableOpacity>
    <TouchableOpacity style={styles.button}
    onPress={()=>{this.laughPage()}}>
    <Text style={styles.para}>
      Laughter is the Best Medicine
    </Text>
    </TouchableOpacity>
    <TouchableOpacity style={styles.button}
    onPress={()=>{this.awarePage()}}>
    <Text style={styles.paragraph}>
      Awareness Games 
    </Text>
    </TouchableOpacity>
   
     </ImageBackground> 
    </View>
  );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    //justifyContent: 'center',
    
    backgroundColor: 'aqua',
    //padding: 8,
  },
  button:{
    //marginLeft:70,
    alignSelf:'center',
    width:200,
    height:80,
    marginTop:50,
    borderRadius:20,
    backgroundColor:'black'

  },
   buttonText:{
    marginLeft:210,
    width:120,
    height:40,
    marginTop:50,
    borderRadius:20,
    backgroundColor:'black',
    textAlign:'center',
    color:'aqua'
  },
  paragraph: {
    margin: 24,
    fontSize: 18,
    fontWeight: 'bold',
    textAlign: 'center',
    alignSelf: 'center',
    color:'aqua'
  },
  para: {
    margin: 24,
    fontSize: 18,
    marginTop:15,
    fontWeight: 'bold',
    textAlign: 'center',
    color:'aqua'
  },
  para1: {
    margin: 24,
    fontSize: 18,
    marginTop:10,
    fontWeight: 'bold',
    textAlign: 'center',
    color:'aqua'
  },
});