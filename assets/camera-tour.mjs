// positions and targets are three-component arrays; times must strictly increase.
export function sampleTour(keys, time) {
  if(keys.length < 2 || keys.some((k,i)=>!Number.isFinite(k.time) || (i && k.time <= keys[i-1].time) || [k.position,k.target].some(v=>!Array.isArray(v)||v.length!==3||v.some(n=>!Number.isFinite(n))))) throw new Error('Invalid camera keyframes');
  let i=0; while(i<keys.length-2 && time>keys[i+1].time)i++;
  const a=keys[i],b=keys[i+1];let u=Math.max(0,Math.min(1,(time-a.time)/(b.time-a.time)));u=u*u*(3-2*u);
  const mix=(x,y)=>x.map((v,j)=>v+(y[j]-v)*u);
  return {position:mix(a.position,b.position),target:mix(a.target,b.target)};
}
