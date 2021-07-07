/** 
A simple ThreeJS/WebGL renderer that takes in a sph-fluid
and renders the positions of the particles
 */


class WaterEngine {
  constructor(fluid){
    this.scene = null;
    this.camera = null; 
    this.renderer = null;
    this.meshes = [];
    this.fluid = fluid;
    this.particles=null;
    
    // Set up all ThreeJS stuff
    this.setup();
    this.initScene();
  }

  clear() {
    for( var i = this.scene.children.length - 1 ; i > 0; i--){
      this.scene.remove(this.scene.children[i]);
    }
  }

  setup(){
    this.scene = new THREE.Scene();

    this.camera = new THREE.PerspectiveCamera( 75, window.innerWidth / window.innerHeight, 1, 10000 );
    this.camera.position.z = 1000;
    this.camera.position.set(WaterEngine.SQUARE_SIZE / 2, WaterEngine.SQUARE_SIZE / 2, WaterEngine.START_OFFSET_Z);

    this.renderer = new THREE.WebGLRenderer();
    this.renderer.setSize( window.innerWidth, window.innerHeight );
    this.renderer.setClearColor( 0xe0e0e0, 1);

    var controls = new THREE.OrbitControls( this.camera, this.renderer.domElement );
    var a = new THREE.Vector3(0,0,0);
    controls.target=a

    // Resizing window
    THREEx.WindowResize(this.renderer, this.camera);
    document.body.appendChild( this.renderer.domElement );

    const axesHelper = new THREE.AxesHelper( 5000 );
    this.scene.add( axesHelper );

    const gridHelper = new THREE.GridHelper(1000, 40);
    this.scene.add(gridHelper);
  };

  initScene() {

    this.clear();
    const geometry = new THREE.BufferGeometry();
    const vertices = [];

    const sprite = new THREE.TextureLoader().load( 'disc.png' );

    for (const position of this.fluid.particlePositions) {
      //console.log(position.x)
      
      vertices.push( position.x, position.y, position.z );
    }

    geometry.setAttribute( 'position', new THREE.Float32BufferAttribute( vertices, 3 ) );

    var material = new THREE.PointsMaterial( { size: WaterEngine.PARTICLE_RADIUS*4, sizeAttenuation: true,map: sprite, alphaTest: 0.5, transparent: true,color: 0x00FFFF} );
    
    this.particles = new THREE.Points( geometry, material );
    this.scene.add( this.particles );

    ////////////////////////////////////////////////////////////////


    //this.clear();
    ////this.drawGrid();
  
    //const geometry = new THREE.CircleGeometry( WaterEngine.PARTICLE_RADIUS, 2 );
    //const material = new THREE.MeshBasicMaterial( {color: 0x2F32D6} );
    //// const material = new THREE.MeshBasicMaterial( {map : new
    //// THREE.TextureLoader().load('../img/circle.png')} );
    //for (const position of this.fluid.particlePositions) {
    //  let mesh = new THREE.Mesh(geometry, material);      
    //  mesh.position.set(position.x, position.y, position.z);
    //  this.meshes.push(mesh);
    //  this.scene.add(mesh);
    //}
  }

  update_(positions) {

    const pos=this.particles.geometry.attributes.position.array;
    //console.log(pos);

    for(let ix=0;ix<pos.length;ix=ix+3){

        pos[ix]=positions[ix/3].x//Math.random() * (5 - (-5)) + (-5)
        pos[ix+1]=positions[ix/3].y
        pos[ix+2]=positions[ix/3].z
    }
    this.particles.geometry.attributes.position.needsUpdate = true;



    //for (let i = 0; i < positions.length; i++) {
    //  this.meshes[i].position.set(
    //      positions[i].x, positions[i].y, positions[i].z);
    //}
  }

  render() {
    requestAnimationFrame( this.render.bind(this) ); 
    this.fluid.calculateAcceleration();
    this.fluid.idle();
    this.update_(this.fluid.particlePositions);
    this.renderer.render( this.scene, this.camera );
  }

  drawGrid() {
    let rectShape = new THREE.Shape();
    rectShape.moveTo(0, 0);
    rectShape.lineTo(0, WaterEngine.SQUARE_SIZE);
    rectShape.lineTo(WaterEngine.SQUARE_SIZE, WaterEngine.SQUARE_SIZE);
    rectShape.lineTo(WaterEngine.SQUARE_SIZE, 0);
    rectShape.lineTo(0, 0);

    const rectGeom = new THREE.ShapeGeometry(rectShape);
    const rectMesh = new THREE.Mesh(
        rectGeom, new THREE.MeshBasicMaterial({color: 0xffffff}));

    const geometry = new THREE.Geometry();
    const material = new THREE.LineBasicMaterial(
        {color: 0xff9b9b, linewidth: WaterEngine.LINE_WIDTH});

    // Draw line outside box
    /*geometry.vertices.push(new THREE.Vector3(-WaterEngine.LINE_WIDTH/2 + 1,
    -WaterEngine.LINE_WIDTH/2, 0));
    geometry.vertices.push(new THREE.Vector3(-WaterEngine.LINE_WIDTH/2 + 1,
    WaterEngine.SQUARE_SIZE + WaterEngine.LINE_WIDTH - 1, 0));

    geometry.vertices.push(new THREE.Vector3(-WaterEngine.LINE_WIDTH/2 + 1,
    WaterEngine.SQUARE_SIZE + WaterEngine.LINE_WIDTH/2 - 1, 0));
    geometry.vertices.push(new THREE.Vector3(WaterEngine.SQUARE_SIZE +
    WaterEngine.LINE_WIDTH - 1, WaterEngine.SQUARE_SIZE +
    WaterEngine.LINE_WIDTH/2 - 1, 0));

    geometry.vertices.push(new THREE.Vector3(WaterEngine.SQUARE_SIZE +
    WaterEngine.LINE_WIDTH/2 - 1, WaterEngine.SQUARE_SIZE +
    WaterEngine.LINE_WIDTH/2- 1, 0));
    geometry.vertices.push(new THREE.Vector3(WaterEngine.SQUARE_SIZE +
    WaterEngine.LINE_WIDTH/2 - 1, -WaterEngine.LINE_WIDTH + 1, 0));

    geometry.vertices.push(new THREE.Vector3(WaterEngine.SQUARE_SIZE +
    WaterEngine.LINE_WIDTH/2 - 1, -WaterEngine.LINE_WIDTH/2 + 1, 0));
    geometry.vertices.push(new THREE.Vector3(-WaterEngine.LINE_WIDTH + 1,
    -WaterEngine.LINE_WIDTH/2 + 1, 0));

    const line = new THREE.Line(geometry, material);
    this.scene.add(line);*/
    this.scene.add(rectMesh)
  };
}

WaterEngine.START_OFFSET_X = 0;
WaterEngine.START_OFFSET_Y = 256;
WaterEngine.START_OFFSET_Z = 0;
WaterEngine.SQUARE_SIZE = 512;
WaterEngine.LINE_WIDTH = 10;
WaterEngine.PARTICLE_RADIUS = 16/2; // h/2
