import * as React from 'react';
import { Text, View, StyleSheet,TouchableOpacity, Image , ImageBackground, ScrollView} from 'react-native';

export default class Norm extends React.Component{
  constructor(){
    super()
    this.state={
      share:'',
      use:'',
      wash:'',
      health:'',
      score1:'',
      questionAnswered1:false
    }
  }
  calculate1=()=>{
    var score1 = 0;
    this.setState({questionAnswered1:true})
    if (this.state.share ==='yes')
      score1 = score1+1
    if (this.state.use ==='yes')
      score1 = score1+1
    if (this.state.wash ==='yes')
      score1 = score1+1
    if (this.state.heath ==='yes')
      score1 = score1+1;
    this.setState({score1:score1,share:'',
      use:'',
      wash:'',
      health:'',})
    
  }

  render(){
    if(this.state.questionAnswered1===true){
    return(
        <View style = {styles.container}>
      <ImageBackground source={require('../assets/Must.png')} style={{alignSelf:'center', width:'100%' ,height:'100%'}}>
      <TouchableOpacity onPress={()=>{this.props.navigation.navigate("Aware")}}>
      <Image style={{width:30,height:30, alignSelf: 'left', marginTop: 0, marginLeft:5,}}source={require('../assets/Backbutton.png')}/>
      </TouchableOpacity>
      <Text style = {styles.paragraph}>Your Score is: {this.state.score1}</Text>
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
      <Image style={{width:30,height:30, alignSelf: 'left', marginTop: 0, marginLeft:5,}}source={require('../assets/Backbutton.png')}/>
      </TouchableOpacity>
      <Text style={styles.paragraph}>
      Are you sharing something hopeful and positive for your friends and family to stay happy during these difficult times?
      </Text>
      <TouchableOpacity style={styles.button}
      onPress={()=>{this.setState({share:'yes'})}}>
      <Text style={styles.para}>
      YES
      </Text>
      </TouchableOpacity>
      <TouchableOpacity style={styles.button}
      onPress={()=>{this.setState({share:'no'})}}>
      <Text style={styles.para}>
      NO
      </Text>
      </TouchableOpacity>
      <Text style={styles.paragraph}>
      Are you making use of the online medium to learn new things? 
      </Text>
      <TouchableOpacity style={styles.button}
      onPress={()=>{this.setState({use:'yes'})}}>
      <Text style={styles.para}>
      YES
      </Text>
      </TouchableOpacity>
      <TouchableOpacity style={styles.button}
      onPress={()=>{this.setState({use:'no'})}}>
      <Text style={styles.para}>
      NO
      </Text>
      </TouchableOpacity>
      <Text style={styles.paragraph}>
      Do yo wash your hands before touching your face?
      </Text>
      <TouchableOpacity style={styles.button}
      onPress={()=>{this.setState({wash:'yes'})}}>
      <Text style={styles.para}>
      YES
      </Text>
      </TouchableOpacity>
      <TouchableOpacity style={styles.button}
      onPress={()=>{this.setState({wash:'no'})}}>
      <Text style={styles.para}>
      NO
      </Text>
      </TouchableOpacity>
      <Text style={styles.paragraph}>
      Do you Follow health workers’ advice and social distancing guidelines if you’ve been advised to do so?
      </Text>
      <TouchableOpacity style={styles.button}
      onPress={()=>{this.setState({health:'yes'})}}>
      <Text style={styles.para}>
      YES
      </Text>
      </TouchableOpacity>
      <TouchableOpacity style={styles.button}
      onPress={()=>{this.setState({share:'no'})}}>
      <Text style={styles.para}>
      NO
      </Text>
      </TouchableOpacity>
      <TouchableOpacity style={styles.buttonText}
      onPress={()=>{this.calculate1()}}>
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
    
    backgroundColor: 'aqua',
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
    marginLeft:70,
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