import * as React from 'react';
import { Text, View, StyleSheet,TouchableOpacity, Image , ImageBackground} from 'react-native';



export default class Laugh extends React.Component {
  render(){
  return (
    <View >
    <ImageBackground source={require('../assets/Must.png')} style={{alignSelf:'center', width:'100%' ,height:'100%'}}>
     <TouchableOpacity 
      onPress={()=>{this.props.navigation.navigate("MainScreen")}}>
      <Image style={{width:280,height:50, alignSelf: 'center', marginTop: 50}}source={require('../assets/COV.png')}/>
      </TouchableOpacity>
      <Text style={styles.paragraph}>
        Memes for you to enjoy 
      </Text>
      <TouchableOpacity onPress={()=>{this.props.navigation.navigate("MainScreen")}}>
      <Image style={{width:30,height:30, alignSelf: 'left', marginTop: 0, marginLeft:5,}}source={require('../assets/Backbutton.png')}/>
      </TouchableOpacity>
      <Image style={{width:280,height:150, alignSelf: 'center', marginTop: 50}}source={require('../assets/Meme1.jpg')}/>
      <Image style={{width:280,height:280, alignSelf: 'center', marginTop: 50}}source={require('../assets/Meme2.jpg')}/>
      <Image style={{width:280,height:230, alignSelf: 'center', marginTop: 50}}source={require('../assets/Meme3.png')}/>
      <Image style={{width:280,height:180, alignSelf: 'center', marginTop: 50}}source={require('../assets/Meme4.png')}/>
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
    backgroundColor:'black'
  },
  paragraph: {
    margin: 26,
    fontSize: 30,
    fontWeight: 'bold',
    textAlign: 'center',
    fontStyle:'italic'
    //backgroundColor:'red'
  },
});