import * as React from 'react';
import { Text, View, StyleSheet,TouchableOpacity,TextInput,Alert,Image, ImageBackground } from 'react-native';
import AppHeader from '../components/AppHeader'
import firebase from 'firebase'
import db from '../config'


export default class LoginScreen extends React.Component {
  constructor(){
    super()
    this.state={
      username:'',
      password:''
    }
  }
  userLogin=async(username,password)=>{
      const response= await firebase.auth().signInWithEmailAndPassword(username,password)
      .then(()=>{this.props.navigation.navigate('MainScreen')})
      .catch(()=>{Alert.alert("Wrong Crededitials")})
      }
  userSignUp=async(username,password)=>{
    if(username && password){
      const response= await firebase.auth().createUserWithEmailAndPassword(username,password)
      .then(()=>{this.props.navigation.navigate('MainScreen')})
      .catch(()=>{Alert.alert("Wrong Crededitials")})}
  
    else{
      Alert.alert('Enter both username and password')
    }
  }
  

      
  render(){
    return(
      <View style = {styles.container}>
       <ImageBackground source={require('../assets/monalisa.jpg')} style={{alignSelf:'center', width:'100%' ,height:'100%'}}>
        
         
          <Text style = {styles.paragraph}>Login Screen</Text>
          <View style={{marginTop:200}}>
          <TextInput style={styles.buttonText}
          placeholder=' Enter email id'
          onChangeText={(text)=>{this.setState({username:text})}}
          value={this.state.username}
          />
          <TextInput style={styles.buttonText}
          placeholder=' Enter password'
          secureTextEntry={true}
          onChangeText={(text)=>{this.setState({password:text})}}
          value={this.state.password}
          />
          <TouchableOpacity style={styles.button}
          onPress={()=>{this.userLogin(this.state.username,this.state.password)}}>
          <Text style={styles.para}>Login</Text>
          </TouchableOpacity>
          <TouchableOpacity style={styles.button}
          onPress={()=>{this.userSignUp(this.state.username,this.state.password)}}>
          <Text style={styles.para}>Sign up</Text>
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
    borderRadius:10,
    borderColor:'blue',
    backgroundColor:'cyan',
    color:'red'
  },
   button:{
    alignSelf: 'center',
    //alignItems:'çenter',
    justifyContent:'center',
    width:200,
    height:60,
    marginTop:30,
    borderRadius:20,
    backgroundColor:'blue',
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
    marginTop: 40,
    fontSize: 28,
    fontWeight: 'bold',
    alignSelf: 'center',
    fontFamily: 'helvetica',
    color:'aqua'
  },
  para:{
    textAlign: 'center',
    fontWeight: 'bold',
    fontFamily: 'helvetica'
  }
})
