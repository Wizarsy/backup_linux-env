#ifdef GL_ES
precision mediump float;
#endif

uniform float u_time;
uniform vec2 u_resolution;
uniform vec2 u_mouse;


vec3 pallete(float t){
  vec3 a = vec3(.5, .5, .5);
  vec3 b = vec3(.5, .5, .5);
  vec3 c = vec3(1., 1., 1.);
  vec3 d = vec3(.263, .416, .557);    
  return a + b * cos(6.28318 * (c * t + d));
}

void main(){
  vec2 uv = (gl_FragCoord.xy * 2.0 - u_resolution.xy ) / u_resolution.y;
  vec2 uv0 = uv;
  vec3 finalColor = vec3(0.);
  
  for (float i = 0. ; i < 4. ; i++){
    uv = fract(uv * 1.5) - 0.5;
    
    float d = length(uv) * exp(-length(uv0));

    vec3 col = pallete(length(uv0) + i * .4 + u_time * .4);

    // d = sin(d * 8. + u_time) / 8.;
    // d = abs(d);
    // d = pow(0.01 / d, 1.2);
    d = pow(0.01 / abs(sin(d * 8. + u_time) / 8.), 1.2);

    finalColor += col * d;
  }
  gl_FragColor = vec4(finalColor, 1.0);
}