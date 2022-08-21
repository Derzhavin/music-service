package com.example.kmmktor

import io.ktor.client.*
import io.ktor.client.request.*
import io.ktor.client.statement.*

class Greeting {
    fun greeting(): String {
        return "Hello, ${Platform().platform}!"
    }
    val client = httpClient()
//    private val client = HttpClient()
    suspend fun getHtml(): String {
//        val response = client.get("https://10.42.0.1:5000")
        val response = client.get("http://10.42.0.1:5000/v1")
        return response.bodyAsText()
    }
}
