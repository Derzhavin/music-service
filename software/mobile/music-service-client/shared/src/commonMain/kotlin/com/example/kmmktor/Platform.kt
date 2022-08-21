package com.example.kmmktor

import io.ktor.client.*

expect fun httpClient(config: HttpClientConfig<*>.() -> Unit = {}): HttpClient

expect class Platform() {
    val platform: String
}