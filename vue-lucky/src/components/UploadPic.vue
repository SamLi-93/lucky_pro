<template>
  <div id="upload">
    <el-upload
      class="upload-demo"
      ref="upload"
      action="http://127.0.0.1:5000/uploadpic"
      :on-preview="handlePreview"
      :before-upload="beforePicUpload"
      :on-remove="handleRemove"
      :on-change="handleChange"
      :file-list="fileList2"
      list-type="picture"
      :on-success = 'handleSuccess'
      :auto-upload="false">
      <el-button slot="trigger" size="small" type="primary">选取文件</el-button>
      <el-button style="margin-left: 10px;" size="small" type="success" @click="submitUpload">上传到服务器</el-button>
      <div slot="tip" class="el-upload__tip">只能上传jpg/png文件，且不超过500kb</div>
    </el-upload>
  </div>
</template>
<script>
  export default {
    data () {
      return {
        fileList2: [],
        test: 'test'
      }
    },
    methods: {
      submitUpload () {
        this.$refs.upload.submit()
      },
      handleSuccess (res, file, fileList) {
        if (res.code === 0) {
          this.$message({
            message: '上传成功！',
            type: 'success'
          })
        } else {
          this.$message({
            message: res.msg,
            type: 'error'
          })
        }
      },
      beforePicUpload (file) {
        let fd = new FormData()
        fd.append('file', file)
        fd.append('test', 'test')
        this.$axios.post('http://127.0.0.1:5000/uploadpic', fd).then((res) => {
          console.log(res)
        }, (res) => {
          console.log(res)
        })
        return false
        // let picSuffix = file.name.split('.')
        // if (picSuffix[1] === 'jpg' || picSuffix[1] === 'png' || picSuffix[1] === 'jpeg') {
        //   return file
        // } else {
        //   this.$message.error('上传文件只能是图片格式!')
        //   return false
        // }
      },
      handleChange (file, fileList) {
        let picSuffix = file.name.split('.')
        if (picSuffix[1] === 'jpg' || picSuffix[1] === 'png' || picSuffix[1] === 'jpeg') {
          return file
        } else {
          console.log(fileList.length)
          console.log(this.fileList2)
          var spliceIndex = (fileList.length - 1)
          fileList.splice(spliceIndex, 1)
          this.$message.error('上传文件只能是图片格式!')
          return false
        }
      },
      handleRemove (file, fileList) {
        console.log(file, fileList)
      },
      handlePreview (file) {
        console.log(file)
      }
    }
  }
</script>

<style scoped>

</style>
