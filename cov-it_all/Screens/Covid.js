import React, { Component } from 'react';
import { Text, View, StyleSheet, Image, TouchableOpacity, ImageBackground } from 'react-native';

export default class App extends Component {
  constructor(){
    super()
    this.state={
      covidcases:''
    }
  }
  getCovidcases=async()=>{
    //var url ='https://covid19.mathdro.id/api/countries/india';
    var url='https://api.covid19india.org/data.json'
    return fetch(url)
    .then(response=>response.json())
    .then(responseJson=>{
      this.setState({
         covidcases:responseJson
      })
    console.log(this.state. covidcases)
    })
    .catch(error=>{
      console.log.error(error)
    })
  }

  componentDidMount=()=>{
    this.getCovidcases()
  }


 

  render() {
    if(this.state. covidcases===''){
      return(
        <View style={styles.conatainer}>
        <Text>Loading..</Text>
        </View>
      )
    }
    else{
      return(
        <View style={styles.container}>
        <ImageBackground source={require('../assets/Must.png')} style={{alignSelf:'center', width:'100%' ,height:'100%'}}>
        <TouchableOpacity 
        onPress={()=>{this.props.navigation.navigate("MainScreen")}}>
        <Image style={{width:280,height:50, alignSelf: 'center', marginTop: 50}}source={require('../assets/COV.png')}/>
        </TouchableOpacity>
        <Text style= {styles.paragraph}>Covid Count in India</Text>
        <TouchableOpacity onPress={()=>{this.props.navigation.navigate("MainScreen")}}>
        <Image style={{width:30,height:30, alignSelf: 'left', marginTop: 0, marginLeft:5,}}source={require('../assets/Backbutton.png')}/>
        </TouchableOpacity>
        <View style={styles.paragraph}>
        <Text style={{fontSize:28,fontWeight: 'bold',fontFamily:'couriernew'}}>Confirmed Cases As of Today</Text>
        <Text style={styles.para}>{this.state .covidcases.statewise[0].confirmed}</Text>
        <Text style={{fontSize:28,fontWeight: 'bold',fontFamily:'couriernew'}}>Active Cases As of Today</Text>
        <Text style= {styles.para}>{this.state. covidcases.statewise[0].active}</Text>
        <Text style={{fontSize:28,fontWeight: 'bold',fontFamily:'couriernew'}}>Recovered Cases As of Today</Text>
        <Text style= {styles.para}>{this.state. covidcases.statewise[0].recovered}</Text>
        </View>
        </ImageBackground>
        </View>
      )
    }
   
 
  }
  
}

const styles = StyleSheet.create({
  container: {
   flex:1
  },
  subContainer : { 
    flex: 1, 
    borderWidth: 1, 
    alignItems: 'center' 
    },
    title:{ 
      marginTop: 50, 
      fontSize: 30,
      fontWeight: '550' 
    },
    cloudImage :{ 
      width: 200, 
      height: 200, 
      marginTop: 30 
    },
    textContainer : { 
      flex: 1,
      alignItems: 'center', 
      flexDirection:'row', 
      marginTop:-150
    },
    paragraph: {
    margin: 24,
    fontSize: 30,
    fontWeight: 'bold',
    textAlign: 'center',
    fontStyle: 'italic'
    //backgroundColor: 'red'
  },
  para: {
    marginTop: 20,
    fontSize: 26,
    fontWeight: 'bold',
    textAlign: 'center',
    fontFamily:'couriernew'
  },
});


const styles1 = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    
    //backgroundColor: 'aqua',
    //padding: 8,
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
    margin: 24,
    fontSize: 30,
    fontWeight: 'bold',
    textAlign: 'center',
    fontStyle: 'italic'
    //backgroundColor: 'red'
  },
});