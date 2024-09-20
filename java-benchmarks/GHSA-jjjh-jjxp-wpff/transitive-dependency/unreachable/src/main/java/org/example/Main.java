package org.example;

import com.fasterxml.jackson.core.JsonParser;
import com.fasterxml.jackson.databind.DeserializationContext;
import com.fasterxml.jackson.datatype.jsr310.deser.DurationDeserializer;
import java.time.Duration;
import java.io.IOException;

public class Main {
  public static void main(String[] args) {
  }

  public Duration deserialize(JsonParser parser, DeserializationContext context) throws IOException {
    return Duration.parse(context.toString());
  }
}