import 'dart:io';
import 'dart:async';
import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

String url = "http://73.215.71.79:5000"; //"http://192.168.0.27:5000";
class Post {
  final String mode;

  Post({this.mode});

  factory Post.fromJson(Map<String, dynamic> json) {
    return Post(mode: json['mode']);
  }

  Map toMap() {
    var map = new Map<String, dynamic>();
    map["mode"] = mode;
    return map;
  }
}

Future<Post> createPost(String url, {Map body}) async {
  return http.post(url, body: body).then((http.Response response) {
    final int statusCode = response.statusCode;

    if (statusCode < 200 || statusCode > 400 || json == null) {
      throw new Exception("Error while fetching data");
    }
    return Post.fromJson(json.decode(response.body));
  });
}


void main() => runApp(MaterialApp(
  home: Scaffold(
    backgroundColor: Colors.grey[900],
    appBar: AppBar(
      title: Text("Rainbow Road"),
      centerTitle: true,
      backgroundColor: Colors.grey[850],
    ),
    body: Padding(
      padding: const EdgeInsets.fromLTRB(30, 40, 30, 0),
      child: Column(
        children: <Widget>[
          SizedBox(
            height: 60.0,
          ),
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: <Widget>[
              Padding(
                padding: const EdgeInsets.all(10.0),
                child: FloatingActionButton(
                  onPressed: () async {
                    Post newPost = new Post(mode: "0");
                    Post p = await createPost(url, body: newPost.toMap());
                    print(p.mode);

                  },
                  backgroundColor: Colors.red[600],
                ),
              ),
              Padding(
                padding: const EdgeInsets.all(10.0),
                child: FloatingActionButton(
                  onPressed: () async {
                    Post newPost = new Post(mode: "1");
                    Post p = await createPost(url, body: newPost.toMap());
                    print(p.mode);

                  },
                  backgroundColor: Colors.pinkAccent[400],
                ),
              ),
              Padding(
                padding: const EdgeInsets.all(10.0),
                child: FloatingActionButton(
                  onPressed: () async {
                    Post newPost = new Post(mode: "2");
                    Post p = await createPost(url, body: newPost.toMap());
                    print(p.mode);

                  },
                  backgroundColor: Colors.pinkAccent,
                ),
              ),
            ],
          ),
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: <Widget>[
              Padding(
                padding: const EdgeInsets.all(10.0),
                child: FloatingActionButton(
                  onPressed: () async {
                    Post newPost = new Post(mode: "3");
                    Post p = await createPost(url, body: newPost.toMap());
                    print(p.mode);

                  },
                  backgroundColor: Colors.blue,
                ),
              ),
              Padding(
                padding: const EdgeInsets.all(10.0),
                child: FloatingActionButton(
                  onPressed: () async {
                    Post newPost = new Post(mode: "4");
                    Post p = await createPost(url, body: newPost.toMap());
                    print(p.mode);

                  },
                  backgroundColor: Colors.lightBlueAccent,
                ),
              ),
              Padding(
                padding: const EdgeInsets.all(10.0),
                child: FloatingActionButton(
                  onPressed: () async {
                    Post newPost = new Post(mode: "5");
                    Post p = await createPost(url, body: newPost.toMap());
                    print(p.mode);

                  },
                  backgroundColor: Colors.cyanAccent,
                ),
              ),
            ],
          ),
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: <Widget>[
              Padding(
                padding: const EdgeInsets.all(10.0),
                child: FloatingActionButton(
                  onPressed: () async {
                    Post newPost = new Post(mode: "6");
                    Post p = await createPost(url, body: newPost.toMap());
                    print(p.mode);

                  },
                  backgroundColor: Colors.tealAccent[400],
                ),
              ),
              Padding(
                padding: const EdgeInsets.all(10.0),
                child: FloatingActionButton(
                  onPressed: () async {
                    Post newPost = new Post(mode: "7");
                    Post p = await createPost(url, body: newPost.toMap());
                    print(p.mode);

                  },
                  backgroundColor: Colors.lightGreenAccent,
                ),
              ),
              Padding(
                padding: const EdgeInsets.all(10.0),
                child: FloatingActionButton(
                  onPressed: () async {
                    Post newPost = new Post(mode: "8");
                    Post p = await createPost(url, body: newPost.toMap());
                    print(p.mode);

                  },
                  backgroundColor: Colors.amber,
                ),
              ),
            ],
          ),
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: <Widget>[
              Padding(
                padding: const EdgeInsets.all(10.0),
                child: FloatingActionButton(
                  onPressed: () async {
                    Post newPost = new Post(mode: "9");
                    Post p = await createPost(url, body: newPost.toMap());
                    print(p.mode);

                  },
                  backgroundColor: Colors.amber[700],
                ),
              ),
              Padding(
                padding: const EdgeInsets.all(10.0),
                child: FloatingActionButton(
                  onPressed: () async {
                    Post newPost = new Post(mode: "10");
                    Post p = await createPost(url, body: newPost.toMap());
                    print(p.mode);

                  },
                  backgroundColor: Colors.amber[900],
                ),
              ),
              Padding(
                padding: const EdgeInsets.all(10.0),
                child: FloatingActionButton(
                  onPressed: () async {
                    Post newPost = new Post(mode: "11");
                    Post p = await createPost(url, body: newPost.toMap());
                    print(p.mode);

                  },
                  backgroundColor: Colors.orange[50],
                ),
              ),
            ],
          ),
          Divider(
            height: 30.0,
            color: Colors.grey[800],
          ),
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: <Widget>[
              Padding(
                padding: const EdgeInsets.all(10.0),
                child: FloatingActionButton(
                  onPressed: () async {
                    Post newPost = new Post(mode: "12");
                    Post p = await createPost(url, body: newPost.toMap());
                    print(p.mode);

                  },
                  backgroundColor: Colors.orange[50],
                ),
              ),
              Padding(
                padding: const EdgeInsets.all(10.0),
                child: FloatingActionButton(
                  onPressed: () async {
                    Post newPost = new Post(mode: "13");
                    Post p = await createPost(url, body: newPost.toMap());
                    print(p.mode);

                  },
                  backgroundColor: Colors.orange[50],
                ),
              ),
              Padding(
                padding: const EdgeInsets.all(10.0),
                child: FloatingActionButton(
                  onPressed: () async {
                    Post newPost = new Post(mode: "14");
                    Post p = await createPost(url, body: newPost.toMap());
                    print(p.mode);

                  },
                  backgroundColor: Colors.orange[50],
                ),
              ),
              Padding(
                padding: const EdgeInsets.all(10.0),
                child: FloatingActionButton(
                  onPressed: () async {
                    Post newPost = new Post(mode: "15");
                    Post p = await createPost(url, body: newPost.toMap());
                    print(p.mode);

                  },
                  backgroundColor: Colors.orange[50],
                ),
              ),
            ],
          ),
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: <Widget>[
              Padding(
                padding: const EdgeInsets.all(10.0),
                child: FloatingActionButton(
                  onPressed: () async {
                    Post newPost = new Post(mode: "16");
                    Post p = await createPost(url, body: newPost.toMap());
                    print(p.mode);

                  },
                  backgroundColor: Colors.orange[50],
                ),
              ),
              Padding(
                padding: const EdgeInsets.all(10.0),
                child: FloatingActionButton(
                  onPressed: () async {
                    Post newPost = new Post(mode: "17");
                    Post p = await createPost(url, body: newPost.toMap());
                    print(p.mode);

                  },
                  backgroundColor: Colors.orange[50],
                ),
              ),
              Padding(
                padding: const EdgeInsets.all(10.0),
                child: FloatingActionButton(
                  onPressed: () async {
                    Post newPost = new Post(mode: "18");
                    Post p = await createPost(url, body: newPost.toMap());
                    print(p.mode);

                  },
                  backgroundColor: Colors.orange[50],
                ),
              ),
              Padding(
                padding: const EdgeInsets.all(10.0),
                child: FloatingActionButton(
                  onPressed: () async {
                    Post newPost = new Post(mode: "19");
                    Post p = await createPost(url, body: newPost.toMap());
                    print(p.mode);

                  },
                  backgroundColor: Colors.orange[50],
                ),
              ),
            ],
          ),

        ],

      ),
    ),


    floatingActionButton: FloatingActionButton(
      onPressed: () async {
            Post newPost = new Post(mode: "-1");
            Post p = await createPost(url, body: newPost.toMap());
            print(p.mode);

      },
      child: Text("off"),
      backgroundColor: Colors.red[600],
    ),

  ),

));



