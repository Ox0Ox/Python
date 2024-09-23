import * as React from 'react';
import { Text, View, StyleSheet,TouchableOpacity, Image, ImageBackground } from 'react-native';



export default class Aware extends React.Component {
  render(){
  return (
    <View style={styles.container} >
    <ImageBackground source={require('../assets/Must.png')} style={{alignSelf:'center', width:'100%' ,height:'100%'}}>
     <TouchableOpacity 
      onPress={()=>{this.props.navigation.navigate("MainScreen")}}>
      <Image style={{width:280,height:50, alignSelf: 'center', marginTop: 50}}source={require('../assets/COV.png')}/>
      </TouchableOpacity>
      <Text style={styles.paragraph}>
        How is your covid knowledge? 
      </Text>
      <TouchableOpacity onPress={()=>{this.props.navigation.navigate("MainScreen")}}>
      <Image style={{width:30,height:30, alignSelf: 'left', marginTop: 0, marginLeft:5,}}source={require('../assets/Backbutton.png')}/>
      </TouchableOpacity>
      <TouchableOpacity style={styles.button}
      onPress={()=>{this.props.navigation.navigate("Myth")}}>
      <Text style={styles.para}>
        Myth VS Truth
      </Text>
      </TouchableOpacity>
      <TouchableOpacity style={styles.button}
      onPress={()=>{this.props.navigation.navigate("Norm")}}>
      <Text style={styles.para}>
        Covid Norms
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
    
    //backgroundColor: 'aqua',
    //padding: 8,
  },
  button:{
    marginLeft:70,
    width:200,
    height:80,
    marginTop:60,
    borderRadius:20,
    backgroundColor:'black'
  },
  paragraph: {
    margin: 24,
    fontSize: 30,
    fontWeight: 'bold',
    textAlign: 'center',
    fontStyle:'italic'
    //backgroundColor: 'red'
  },
  para: {
    //margin: 24,
    fontSize: 18,
    marginTop:25,
    fontWeight: 'bold',
    textAlign: 'center',
    color:'aqua',
    //justifyContent:'center'
  },
});