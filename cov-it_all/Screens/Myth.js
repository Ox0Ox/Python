import * as React from 'react';
import { Text, View, StyleSheet,TouchableOpacity, Image,ScrollView, ImageBackground } from 'react-native';

export default class Myth extends React.Component{
  constructor(){
    super()
    this.state={
      vaccine:'',
      sunny:'',
      rich:'',
      tell:'',
      score:'',
      questionAnswered:false
    }
  }
  calculate=()=>{
    var score = 0;
    this.setState({questionAnswered:true})
    if (this.state.vaccine ==='yes')
      score = score+1
    if (this.state.sunny ==='no')
      score = score+1
    if (this.state.rich ==='no')
      score = score+1
    if (this.state.vaccine ==='no')
      score = score+1;
    this.setState({score:score,vaccine:'',
      sunny:'',
      rich:'',
      tell:'',})
    
  }
  render(){
    if(this.state.questionAnswered===true){
    return(
       <View style = {styles.container}>
      <ImageBackground source={require('../assets/Must.png')} style={{alignSelf:'center', width:'100%' ,height:'100%'}}>
      <TouchableOpacity onPress={()=>{this.props.navigation.navigate("Aware")}}>
      <Image style={{width:30,height:30, alignSelf: 'left', marginTop: 30, marginLeft:5,}}source={require('../assets/Backbutton.png')}/>
      </TouchableOpacity>
      <Text style = {styles.paragraph}>Your Score is: {this.state.score}</Text>
      </ImageBackground>
      </View>
    )
    }
    else{
    return(
      <View>
      <ScrollView style={{width:"100%"}}>
      <ImageBackground source={require('../assets/Must.png')} style={{alignSelf:'center', width:'100%' ,height:'100%'}}>
       <TouchableOpacity onPress={()=>{this.props.navigation.navigate("Aware")}}>
      <Image style={{width:30,height:30, alignSelf: 'left', marginTop: 30, marginLeft:5,}}source={require('../assets/Backbutton.png')}/>
      </TouchableOpacity>
      <Text style={styles.paragraph}>
      Vaccines are harmful for our health.
      </Text>
      <TouchableOpacity style={styles.button}
      onPress={()=>{this.setState({vaccine:'yes'})}}>
      <Text style={styles.para}>
      YES
      </Text>
      </TouchableOpacity>
      <TouchableOpacity style={styles.button}
      onPress={()=>{this.setState({vaccine:'no'})}}>
      <Text style={styles.para}>
      NO
      </Text>
      </TouchableOpacity>
      <Text style={styles.paragraph}>
      COVID-19 can’t be passed on warm sunny weather.
      </Text>
      <TouchableOpacity style={styles.button}
      onPress={()=>{this.setState({sunny:'yes'})}}>
      <Text style={styles.para}>
      YES
      </Text>
      </TouchableOpacity>
      <TouchableOpacity style={styles.button}
      onPress={()=>{this.setState({sunny:'no'})}}>
      <Text style={styles.para}>
      NO
      </Text>
      </TouchableOpacity>
      <Text style={styles.paragraph}>
      COVID-19 only affects rich people.
      </Text>
      <TouchableOpacity style={styles.button}
      onPress={()=>{this.setState({rich:'yes'})}}>
      <Text style={styles.para}>
      YES
      </Text>
      </TouchableOpacity>
      <TouchableOpacity style={styles.button}
      onPress={()=>{this.setState({rich:'no'})}}>
      <Text style={styles.para}>
      NO
      </Text>
      </TouchableOpacity>
      <Text style={styles.paragraph}>
      You can always tell if someone has COVID-19.
      </Text>
      <TouchableOpacity style={styles.button}
      onPress={()=>{this.setState({tell:'yes'})}}>
      <Text style={styles.para}>
      YES
      </Text>
      </TouchableOpacity>
      <TouchableOpacity style={styles.button}
      onPress={()=>{this.setState({tell:'no'})}}>
      <Text style={styles.para}>
      NO
      </Text>
      </TouchableOpacity>
      <TouchableOpacity style={styles.buttonText}
      onPress={()=>{this.calculate()}}>
      <Text style={styles.para1}>
      Submit
      </Text>
      </TouchableOpacity>
      </ImageBackground>
      </ScrollView>
      </View>
    );
    }
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
    alignSelf: 'center',
    width:100,
    height:80,
    marginTop:20,
    borderRadius:20,
    backgroundColor:'black'
  },
   buttonText:{
    alignSelf: 'center',
    width:200,
    height:40,
    marginTop:50,
    borderRadius:20,
    backgroundColor:'red',
    color:'white'
  },
  paragraph: {
    margin: 24,
    fontSize: 26,
    fontWeight: 'bold',
    textAlign: 'center',
    color:'Black'
  },
  para: {
    margin: 24,
    fontSize: 18,
    marginTop:25,
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